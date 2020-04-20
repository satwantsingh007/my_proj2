
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name = 'project'),
    path('<int:proj_id>/', views.detail,name = 'detail'),
]