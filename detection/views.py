from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from ultralytics import YOLO
import cv2
import numpy as np
import os
import base64
from django.conf import settings
from .models import DetectionRecord
from .serializers import DetectionRecordSerializer

# 模型路径
MODEL_PATH = os.path.join(settings.BASE_DIR, 'exp21', 'weights', 'best.pt')

# 全局加载模型
try:
    model = YOLO(MODEL_PATH)
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

# 文化信息映射
PATTERN_INFO = {
    'sun': {
        'label': '太阳纹',
        'era': '战国至清代',
        'region': '广西、云南广泛分布（北流型/灵山型常见）',
        'desc': '铜鼓面中心的典型纹饰，象征太阳崇拜。'
    },
    'wa': {
        'label': '蛙纹',
        'era': '东汉至隋唐',
        'region': '滇系及越系铜鼓（石寨山型/冷水冲型）',
        'desc': '立体或平面蛙饰，反映稻作文化中的求雨信仰。'
    },
    'lei': {
        'label': '云雷纹',
        'era': '春秋至宋代',
        'region': '中原影响下的南方各型铜鼓',
        'desc': '由云纹和雷纹组成的几何图案，象征风雷。'
    }
}

@api_view(['POST'])
@permission_classes([AllowAny])
def detect_patterns(request):
    """
    铜鼓纹样检测接口
    """
    if model is None:
        return Response({'message': '模型加载失败'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if 'image' not in request.FILES:
        return Response({'message': '请上传图片'}, status=status.HTTP_400_BAD_REQUEST)

    image_file = request.FILES['image']
    
    # 验证文件类型
    allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    ext = os.path.splitext(image_file.name)[1].lower()
    if ext not in allowed_extensions:
        return Response({'message': '仅支持 JPG、PNG、GIF 格式的图片'}, status=status.HTTP_400_BAD_REQUEST)
    
    # 验证文件大小（限制为50MB）
    max_size = 50 * 1024 * 1024  # 50MB
    if image_file.size > max_size:
        return Response({'message': '图片大小不能超过50MB'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        file_bytes = np.frombuffer(image_file.read(), np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        
        if img is None:
            return Response({'message': '图片解析失败'}, status=status.HTTP_400_BAD_REQUEST)

        results = model(img)
        result = results[0]
        
        detections = []
        for box in result.boxes:
            conf = float(box.conf[0])
            cls_id = int(box.cls[0])
            raw_label = result.names[cls_id]
            
            info = PATTERN_INFO.get(raw_label, {
                'label': raw_label, 'era': '未知', 'region': '未知'
            })
            
            detections.append({
                'label': info['label'],
                'confidence': conf,
                'era': info['era'],
                'region': info['region'],
                'bbox': box.xyxy[0].tolist()
            })

        # 绘制结果
        annotated_img = result.plot()
        # 确保图像是 uint8 类型
        annotated_img = annotated_img.astype(np.uint8)
        
        # 压缩图片：如果图片太大，进行缩放
        max_size = 800
        height, width = annotated_img.shape[:2]
        if width > max_size or height > max_size:
            scale = max_size / max(width, height)
            new_width = int(width * scale)
            new_height = int(height * scale)
            annotated_img = cv2.resize(annotated_img, (new_width, new_height), interpolation=cv2.INTER_AREA)
        
        # 使用 cv2.imencode 并正确处理 buffer，降低质量以减少大小
        params = [cv2.IMWRITE_JPEG_QUALITY, 85]
        success, buffer = cv2.imencode('.jpg', annotated_img, params)
        if not success:
            return Response({'message': '图片编码失败'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        # 将 buffer 转换为 bytes
        buffer_bytes = np.array(buffer).tobytes()
        img_base64 = base64.b64encode(buffer_bytes).decode('utf-8')

        return Response({
            'message': '检测成功',
            'detections': detections,
            'image_data': f"data:image/jpeg;base64,{img_base64}"
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'message': f'出错: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_detection_record(request):
    """
    保存检测记录
    """
    data = request.data.copy()
    data['user'] = request.user.id

    # 处理标注图片：如果是 base64 字符串，转换为图片文件
    if 'annotated_image_data' in data and data['annotated_image_data']:
        try:
            import base64
            from django.core.files.base import ContentFile
            from datetime import datetime

            base64_str = str(data['annotated_image_data'])

            # 解码 base64 数据
            if ',' in base64_str:
                # 移除 data:image/png;base64, 前缀
                format_str, base64_str = base64_str.split(',', 1)
                image_format = format_str.split(';')[0].split('/')[-1]
            else:
                image_format = 'png'

            # 解码并保存为图片文件
            image_data = base64.b64decode(base64_str)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"annotated_{timestamp}.png"

            # 创建 ContentFile 对象
            image_file = ContentFile(image_data, name=filename)

            # 添加到 data 中，让 serializer 保存
            data['annotated_image'] = image_file

        except Exception as e:
            return Response(
                {'message': f'图片处理失败：{str(e)}'},
                status=status.HTTP_400_BAD_REQUEST
            )

    serializer = DetectionRecordSerializer(data=data)
    if serializer.is_valid():
        record = serializer.save()

        # 生成 Markdown 文档
        try:
            from django.conf import settings
            from datetime import datetime

            # 创建 markdown 文件目录
            md_dir = settings.MEDIA_ROOT / 'detections' / 'markdown'
            md_dir.mkdir(parents=True, exist_ok=True)

            # 生成文件名
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            md_filename = f"detection_{timestamp}_{record.id}.md"
            md_filepath = md_dir / md_filename

            # 生成 markdown 内容
            md_content = f"""# 铜鼓纹样检测报告

## 基本信息
- **检测时间**: {record.created_at.strftime('%Y-%m-%d %H:%M:%S')}
- **纹样类型**: {record.pattern_type}
- **年代推测**: {record.era_estimate}
- **地域类型**: {record.region_type}
- **置信度**: {record.confidence:.2%}

## 个人备注
{record.remark if record.remark else '无'}

## 标注图片

![标注图片](file:///{settings.MEDIA_ROOT.as_posix()}/{record.annotated_image})

"""

            # 保存 markdown 文件
            with open(md_filepath, 'w', encoding='utf-8') as f:
                f.write(md_content)
        except Exception as e:
            pass

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_records(request):
    """
    获取当前用户的检测历史
    """
    records = DetectionRecord.objects.filter(user=request.user)
    serializer = DetectionRecordSerializer(records, many=True)
    return Response(serializer.data)
