
from django.views.generic import TemplateView

from django.contrib import admin
from django.urls import path

from django.urls import include, path

urlpatterns = [
    path('', TemplateView.as_view(template_name='chat/index.html'), name='home'),
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
]
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
