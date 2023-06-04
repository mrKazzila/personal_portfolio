from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from my_portfolio import views

urlpatterns = [
    path('enter2admin/', admin.site.urls, 'admin'),
    path('', views.HomeView.as_view(), name='home'),
    path('blog/', include('blog.urls'), name='blog'),
]

urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
