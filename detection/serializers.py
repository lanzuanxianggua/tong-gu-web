from rest_framework import serializers
from .models import DetectionRecord
import base64
from django.conf import settings

class DetectionRecordSerializer(serializers.ModelSerializer):
    """
    检测记录的序列化器类
    用于将 DetectionRecord 模型实例转换为 JSON 格式，反之亦然
    继承自 ModelSerializer，可以自动根据模型生成字段
    """
    # 添加计算字段，用于返回图片的 base64 数据
    annotated_image_data = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    
    class Meta:
        model = DetectionRecord
        fields = '__all__'
    
    def get_annotated_image_data(self, obj):
        """
        获取标注图片的 base64 数据
        如果 annotated_image 存在，读取文件并转换为 base64 格式
        """
        if obj.annotated_image:
            try:
                image_path = obj.annotated_image.path
                with open(image_path, 'rb') as f:
                    image_data = f.read()
                    base64_data = base64.b64encode(image_data).decode('utf-8')
                    if image_path.endswith('.jpg') or image_path.endswith('.jpeg'):
                        return f"data:image/jpeg;base64,{base64_data}"
                    else:
                        return f"data:image/png;base64,{base64_data}"
            except Exception as e:
                return None
        return None
