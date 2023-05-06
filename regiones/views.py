from rest_framework.response import Response
from rest_framework import status, generics, filters
from django.http import Http404
from .serializer import ComunaSerializer, ProvinciaSerializer, RegionSerializer
from .models import Region, Provincia, Comuna
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

class ListaRegionesView(generics.ListCreateAPIView):

    queryset = Region.objects.all().order_by("nombre")
    serializer_class = RegionSerializer
    permission_classes = [AllowAny]
    parser_classes = [JSONParser]
    pagination_class = PageNumberPagination

    def list(self, request, format=None):

        regiones = self.get_queryset()
        pagina = self.paginate_queryset(regiones)
        serializer = self.get_serializer(pagina, many=True)

        if len(serializer.data):
            return self.get_paginated_response(serializer.data)
        
        return Response({"message": "No hay Regiones Registradas"}, status=status.HTTP_204_NO_CONTENT)
    
    def create(self, request, format=None):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            
            serializer.save()
            return Response({"data":serializer.data, "message": "region creada con exito"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleRegionView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = RegionSerializer
    permission_classes = [AllowAny]

    def get_object(self, id:int):

        try:
            region = Region.objects.get(id_region = id)
        except Region.DoesNotExist:
            raise Http404

        return region
    
    def get(self, request, id:int, format=None):

        region = self.get_object(id)
        serializer = self.get_serializer(region)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, id:int, fromat=None):

        region = self.get_object(id)
        serializer = RegionSerializer(region, data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response({"data":serializer.data, "message": "region actualizada con exito"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, id:int, format=None):

        region = self.get_object(id)
        region.delete()

        return Response({"message": "La region a sido eliminada con exito"}, status=status.HTTP_204_NO_CONTENT)

class RegionSearchView(generics.ListAPIView):

    permission_classes = [AllowAny]
    serializer_class = RegionSerializer

    def list(self, request, format=None):

        nombre = request.GET.get("search")
        filter = Region.objects.filter(nombre=nombre)
        serializer = self.get_serializer(filter, many=True)

        if not len(serializer.data):
            return Response({"data": "no se encontraron regiones con ese nombre"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)