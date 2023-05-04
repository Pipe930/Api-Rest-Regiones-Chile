from rest_framework.response import Response
from rest_framework import status, generics
from django.http import Http404
from .serializer import ComunaSerializer, ProvinciaSerializer, RegionSerializer
from .models import Region, Provincia, Comuna
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

class ListaRegionesView(generics.ListAPIView):

    queryset = Region.objects.all().order_by("nombre")
    serializer_class = RegionSerializer
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination

    def get(self, request, format=None):

        regiones = self.get_queryset()
        pagina = self.paginate_queryset(regiones)
        serializer = self.get_serializer(pagina, many=True)

        if len(serializer.data):
            return self.get_paginated_response(serializer.data)
        
        return Response({"message": "No hay Regiones Registradas"}, status=status.HTTP_204_NO_CONTENT)

class DetalleRegionView(generics.RetrieveAPIView):

    serializer_class = RegionSerializer
    permission_classes = [AllowAny]

    def get_object(self, id:int):

        try:
            region = Region.objects.get(id_region = id)
        except Region.DoesNotExist:
            raise Http404

        return region
    
    def get(self, request, id:int, format=None):

        region = self.get_object(id=id)

        serializer = self.get_serializer(region)

        return Response(serializer.data, status=status.HTTP_200_OK)