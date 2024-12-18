from django.urls import path
from . import views
from .views import update_task_status, create_task

urlpatterns = [
    path('tcc/<int:tcc_id>/', views.tcc_view, name='tcc'),
    path('tcc/<int:tcc_id>/edit/', views.tcc_edit, name='tcc_edit'),
    path('tcc/<int:tcc_id>/update_task_status/', views.update_task_status, name='update_task_status'),
    path('create-task/<int:tcc_id>/', create_task, name='create_task'),
]
