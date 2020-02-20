from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from django.conf.urls import url

urlpatterns = [
    url("admin/", admin.site.urls),
    path("api/v1/users/", include("user.urls")),
    path("api/v1/emrif/", include("emrif.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
