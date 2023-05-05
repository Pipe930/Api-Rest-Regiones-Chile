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

    def get(self, request, format=None):

        regiones = self.get_queryset()
        pagina = self.paginate_queryset(regiones)
        serializer = self.get_serializer(pagina, many=True)

        if len(serializer.data):
            return self.get_paginated_response(serializer.data)
        
        return Response({"message": "No hay Regiones Registradas"}, status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request, format=None):

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
    
    def put(self, request, id:int, fromat=None):

        region = self.get_object(id)
        serializer = RegionSerializer(region, data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response({"data":serializer.data, "message": "region actualizada con exito"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegionSearchView(generics.ListAPIView):

    queryset = Region.objects.all().order_by('nombre')
    serializer_class = RegionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre']
    permission_classes = [AllowAny]