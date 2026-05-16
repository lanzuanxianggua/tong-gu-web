from rest_framework import serializers
from .models import DetectionRecord
import base64


class DetectionRecordListSerializer(serializers.ModelSerializer):
    """列表查询使用，包含标注图片 URL"""
    annotated_image_url = serializers.SerializerMethodField()

    class Meta:
        model = DetectionRecord
        fields = ['id', 'user', 'original_image', 'annotated_image',
                  'annotated_image_url', 'pattern_type', 'era_estimate',
                  'region_type', 'confidence', 'remark', 'created_at']
        read_only_fields = ['user', 'created_at']

    def get_annotated_image_url(self, obj):
        if obj.annotated_image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.annotated_image.url)
            return obj.annotated_image.url
        return None


class DetectionRecordSerializer(serializers.ModelSerializer):
    annotated_image_data = serializers.SerializerMethodField()

    class Meta:
        model = DetectionRecord
        fields = '__all__'
        read_only_fields = ['user', 'created_at']

    def get_annotated_image_data(self, obj):
        if obj.annotated_image:
            try:
                image_path = obj.annotated_image.path
                with open(image_path, 'rb') as f:
                    image_data = f.read()
                    b64 = base64.b64encode(image_data).decode('utf-8')
                    if image_path.lower().endswith(('.jpg', '.jpeg')):
                        return f"data:image/jpeg;base64,{b64}"
                    return f"data:image/png;base64,{b64}"
            except Exception:
                return None
        return None
