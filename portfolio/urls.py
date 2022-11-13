from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('base', views.base, name='base'),
    path('<int:pk>', views.project_detail, name='project_detail'),
]