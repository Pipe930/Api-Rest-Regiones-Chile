
from django.contrib import admin
from django.urls import path, include
from regiones.urls import urlRegion

urlApi = [
    path("regiones/", include(urlRegion))
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(urlApi))
]
