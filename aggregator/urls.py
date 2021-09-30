from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name="news"),
    path('news-url-tracking/<str:pk>/', views.urlClickTracking, name="news-url-tracking"),
]
