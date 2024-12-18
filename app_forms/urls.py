from django.urls import path
from .views import criar_tcc, dashboard
from app_forms import views  

urlpatterns = [
    path('criar_tcc/', criar_tcc, name='criar_tcc'),
    path('dashboard/', dashboard, name='dashboard'),
    path('tasks/add/', views.add_task, name='add_task'),
    path('tcc/<int:tcc_id>/', views.tcc_details, name='tcc_details'),
    path('tasks/toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
