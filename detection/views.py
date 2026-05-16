from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from ultralytics import YOLO
import cv2
import numpy as np
import os
import base64
import logging
from django.conf import settings
from django.core.paginator import Paginator
from backend.utils import error_response
from .models import DetectionRecord
from .serializers import DetectionRecordSerializer, DetectionRecordListSerializer

logger = logging.getLogger(__name__)

MODEL_PATH = os.path.join(settings.BASE_DIR, 'exp21', 'weights', 'best.pt')

try:
    model = YOLO(MODEL_PATH)
except Exception as e:
    logger.error(f"Error loading YOLO model: {e}")
    model = None

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


def error_response(message, errors=None, status_code=status.HTTP_400_BAD_REQUEST):
    resp = {'message': message}
    if errors:
        resp['errors'] = errors
    return Response(resp, status=status_code)


@api_view(['POST'])
@permission_classes([AllowAny])
def detect_patterns(request):
    if model is None:
        return error_response('模型加载失败，请稍后重试', status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

    if 'image' not in request.FILES:
        return error_response('请上传图片')

    image_file = request.FILES['image']

    allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    ext = os.path.splitext(image_file.name)[1].lower()
    if ext not in allowed_extensions:
        return error_response('仅支持 JPG、PNG、GIF 格式的图片')

    max_size = 50 * 1024 * 1024
    if image_file.size > max_size:
        return error_response('图片大小不能超过50MB')

    try:
        file_bytes = np.frombuffer(image_file.read(), np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        if img is None:
            return error_response('图片解析失败，请检查文件格式')

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

        annotated_img = result.plot()
        annotated_img = annotated_img.astype(np.uint8)

        max_dim = 800
        height, width = annotated_img.shape[:2]
        if width > max_dim or height > max_dim:
            scale = max_dim / max(width, height)
            new_width = int(width * scale)
            new_height = int(height * scale)
            annotated_img = cv2.resize(annotated_img, (new_width, new_height), interpolation=cv2.INTER_AREA)

        params = [cv2.IMWRITE_JPEG_QUALITY, 85]
        success, buffer = cv2.imencode('.jpg', annotated_img, params)
        if not success:
            return error_response('图片编码失败', status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

        buffer_bytes = np.array(buffer).tobytes()
        img_base64 = base64.b64encode(buffer_bytes).decode('utf-8')

        return Response({
            'message': '检测成功',
            'detections': detections,
            'image_data': f"data:image/jpeg;base64,{img_base64}"
        }, status=status.HTTP_200_OK)

    except Exception as e:
        logger.error(f'Detection error: {e}')
        return error_response('检测过程出错，请稍后重试', status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_detection_record(request):
    data = request.data.copy()
    data['user'] = request.user.id

    if 'annotated_image_data' in data and data['annotated_image_data']:
        try:
            from django.core.files.base import ContentFile
            from datetime import datetime

            base64_str = str(data['annotated_image_data'])

            if ',' in base64_str:
                format_str, base64_str = base64_str.split(',', 1)

            # 验证 base64 数据大小（解码后不超过 50MB）
            if len(base64_str) * 3 // 4 > 50 * 1024 * 1024:
                return error_response('标注图片数据过大')

            image_data = base64.b64decode(base64_str)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"annotated_{timestamp}.jpg"
            image_file = ContentFile(image_data, name=filename)
            data['annotated_image'] = image_file

        except Exception as e:
            return error_response(f'图片处理失败：{str(e)}')

    serializer = DetectionRecordSerializer(data=data)
    if serializer.is_valid():
        record = serializer.save(user=request.user)

        try:
            from datetime import datetime as dt
            md_dir = settings.MEDIA_ROOT / 'detections' / 'markdown'
            md_dir.mkdir(parents=True, exist_ok=True)

            ts = dt.now().strftime('%Y%m%d_%H%M%S')
            md_filename = f"detection_{ts}_{record.id}.md"
            md_filepath = md_dir / md_filename

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
            with open(md_filepath, 'w', encoding='utf-8') as f:
                f.write(md_content)
        except Exception as e:
            logger.warning(f'Markdown report generation failed: {e}')

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return error_response('保存记录失败', serializer.errors)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_records(request):
    records = DetectionRecord.objects.filter(user=request.user).order_by('-created_at')

    try:
        page_num = max(1, int(request.query_params.get('page', 1)))
        page_size = min(100, max(1, int(request.query_params.get('page_size', 10))))
    except (ValueError, TypeError):
        return error_response('分页参数无效')

    paginator = Paginator(records, page_size)
    page = paginator.get_page(page_num)

    serializer = DetectionRecordListSerializer(page.object_list, many=True, context={'request': request})

    return Response({
        'results': serializer.data,
        'count': paginator.count,
        'total_pages': paginator.num_pages,
        'current_page': page.number,
    })


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_detection_record(request, record_id):
    try:
        record = DetectionRecord.objects.get(id=record_id, user=request.user)
        record.delete()
        return Response({'message': '记录已删除'}, status=status.HTTP_200_OK)
    except DetectionRecord.DoesNotExist:
        return error_response('记录不存在', status_code=status.HTTP_404_NOT_FOUND)
