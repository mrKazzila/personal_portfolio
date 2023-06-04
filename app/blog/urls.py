from django.urls import path

from .views import BlogView, detail

app_name = 'blog'

urlpatterns = [
    path('', BlogView.as_view(), name='blogs'),
    path('<int:blog_id>/', detail, name='detail'),
]
