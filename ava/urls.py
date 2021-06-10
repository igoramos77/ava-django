from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from aplic.urls import router

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path("", include("enter.urls")),
    path('dashboard/', include('aplic.urls')),
    path('auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
