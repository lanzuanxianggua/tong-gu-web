from django.urls import path
from .views import detect_patterns, save_detection_record, get_user_records, delete_detection_record

urlpatterns = [
    path('detect/', detect_patterns, name='detect_patterns'),
    path('save-record/', save_detection_record, name='save_detection_record'),
    path('my-records/', get_user_records, name='get_user_records'),
    path('delete-record/<int:record_id>/', delete_detection_record, name='delete_detection_record'),
]
