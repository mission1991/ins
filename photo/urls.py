from django.urls import path
from .views import *

app_name = 'photo'

urlpatterns = [
    path('', photo_list, name='게시글리스트'),
    path('upload/', PhotoUploadView.as_view(), name='게시글올리기'),
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name='게시글삭제'),
    path('update/<int:pk>/', PhotoUpdateView.as_view(), name='게시글수정'),
    path('detail/<int:pk>/', PhotoDetailView.as_view(), name='게시글정보')
]