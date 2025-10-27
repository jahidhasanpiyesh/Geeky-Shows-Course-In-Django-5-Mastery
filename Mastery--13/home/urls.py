from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('demo/', views.demo_view, name='demo_view')
]
