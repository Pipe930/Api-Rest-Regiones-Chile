
from django.contrib import admin
from django.urls import path, include
from regiones.urls import urlRegion

urlpatterns = [
    path("admin/", admin.site.urls),
    path("regiones/", include(urlRegion))
]
