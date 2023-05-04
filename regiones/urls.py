from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlRegion = [
    path("", views.ListaRegionesView.as_view(), name="listaregiones"),
    path("region/<int:id>", views.DetalleRegionView.as_view(), name="detalleregion")
]

urlRegion = format_suffix_patterns(urlpatterns=urlRegion)