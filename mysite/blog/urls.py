from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.PostView.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail')
]
