from django.db import models
from django.conf import settings
import base64
import io
from datetime import datetime
from django.core.files.base import ContentFile
from PIL import Image

class DetectionRecord(models.Model):
    """
    铜鼓纹样检测记录模型
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='detection_records',
        null=True,
        blank=True,
        verbose_name='用户'
    )
    original_image = models.ImageField(upload_to='detections/original/', verbose_name='原图', null=True, blank=True)
    annotated_image = models.ImageField(upload_to='detections/annotated/', verbose_name='标注图', null=True, blank=True)
    annotated_image_data = models.TextField(verbose_name='标注图数据 (Base64)', blank=True, null=True)
    
    pattern_type = models.CharField(max_length=100, verbose_name='纹样类型')
    era_estimate = models.CharField(max_length=100, verbose_name='年代推测')
    region_type = models.CharField(max_length=100, verbose_name='地域类型')
    confidence = models.FloatField(verbose_name='置信度')
    
    remark = models.TextField(blank=True, null=True, verbose_name='个人备注')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='检测时间')

    class Meta:
    # 设置模型的单数可读名称，用于在 Django admin 界面显示
        verbose_name = '检测记录'
    # 设置模型的复数可读名称，用于在 Django admin 界面显示
        verbose_name_plural = '检测记录'
    # 设置模型的默认排序方式，按照创建时间降序排列
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        # 如果有 annotated_image_data 但没有实际文件，需要创建文件
        if self.annotated_image_data and not self.annotated_image:
            # 解码 base64 数据
            format_str, base64_str = self.annotated_image_data.split(',', 1)
            image_format = format_str.split(';')[0].split('/')[-1]
            image_data = base64.b64decode(base64_str)
            
            # 使用 PIL 打开并压缩图片
            img = Image.open(io.BytesIO(image_data))
            
            # 如果图片太大，进行缩放
            max_size = (800, 800)
            if img.size[0] > max_size[0] or img.size[1] > max_size[1]:
                img.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            # 转换为 RGB 模式（如果需要）
            if img.mode in ('RGBA', 'LA', 'P'):
                img = img.convert('RGB')
            
            # 保存到内存缓冲区
            buffer = io.BytesIO()
            img.save(buffer, format='JPEG', quality=85, optimize=True)
            buffer.seek(0)
            
            # 生成文件名
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"annotated_{timestamp}.jpg"
            
            # 创建 ContentFile 对象
            image_file = ContentFile(buffer.getvalue(), name=filename)
            
            # 设置到 annotated_image 字段
            self.annotated_image = image_file
            
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.pattern_type} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
