
from django.contrib import admin
from django.urls import path, include
from regiones.urls import urlRegion, urlProvincia, urlComuna

urlApi = [
    path("regiones/", include(urlRegion)),
    path("provincias/", include(urlProvincia)),
    path("comunas/", include(urlComuna))
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(urlApi))
]
