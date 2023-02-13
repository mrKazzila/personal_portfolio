from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogView.as_view(), name='blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
