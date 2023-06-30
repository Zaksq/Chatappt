from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='index'),
    path('send_message/', views.send_message, name='send_message'),
    path('change_background/', views.change_background, name='change_background'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
