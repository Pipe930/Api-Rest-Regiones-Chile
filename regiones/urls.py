from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlRegion = [
    path("", views.ListaRegionesView.as_view(), name="listaregiones"),
    path("region/<int:id>", views.DetalleRegionView.as_view(), name="detalleregion"),
    path("region", views.RegionSearchView.as_view(), name="searchregion")
]

urlProvincia = [
    path("", views.ListaProvinciaView.as_view(), name="listaprovincias"),
    path("provincia/<int:id>", views.DetalleProvinciaView.as_view(), name="detalleprovincia")
]

urlComuna = [
    path("", views.ListaComunasView.as_view(), name="listacomunas")
]

urlComuna = format_suffix_patterns(urlComuna)
urlProvincia = format_suffix_patterns(urlProvincia)
urlRegion = format_suffix_patterns(urlRegion)