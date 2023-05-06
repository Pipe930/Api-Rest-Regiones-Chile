from typing import Any
from rest_framework.response import Response
from rest_framework import status, generics, filters
from django.http import Http404
from .serializer import ComunaSerializer, ProvinciaSerializer, RegionSerializer
from .models import Region, Provincia, Comuna
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination, DjangoPaginator

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

        if not len(serializer.data):
            return Response({"message": "No hay Regiones Registradas"}, status=status.HTTP_204_NO_CONTENT)
        
        return self.get_paginated_response(serializer.data)
    
    def post(self, request, format=None):

        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
        
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response({"data":serializer.data, "message": "region creada con exito"}, status=status.HTTP_201_CREATED)

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
        serializer = self.get_serializer(region, data=request.data)

        if not serializer.is_valid():

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response({"data":serializer.data, "message": "region actualizada con exito"}, status=status.HTTP_200_OK)

    
    def delete(self, request, id:int, format=None):

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

class ListaProvinciaView(generics.ListCreateAPIView):

    parser_classes = [JSONParser]
    permission_classes = [AllowAny]
    queryset = Provincia.objects.all().order_by("nombre")
    serializer_class = ProvinciaSerializer
    pagination_class = PageNumberPagination

    def get(self, request, format=None):

        provincias = self.get_queryset()
        page = self.paginate_queryset(provincias)
        serializer = self.get_serializer(page, many=True)

        if not len(serializer.data):
            return Response({"message": "No hay provincias registradas"}, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):

        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response({"data": serializer.data, "message": "se creo la provincia con exito"}, status=status.HTTP_201_CREATED)

class DetalleProvinciaView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ProvinciaSerializer
    permission_classes = [AllowAny]

    def get_object(self, id:int):

        try:
            provincia = Provincia.objects.get(id_provincia = id)
        except Provincia.DoesNotExist:
            raise Http404

        return provincia
    
    def get(self, request, id:int, format=None):

        provincia = self.get_object(id)
        serializer = self.get_serializer(provincia)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id:int, fromat=None):

        provincia = self.get_object(id)
        serializer = self.get_serializer(provincia, data=request.data)

        if not serializer.is_valid():

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response({"data":serializer.data, "message": "Provincia actualizada con exito"}, status=status.HTTP_200_OK)
    
    def delete(self, request, id:int, format=None):

        provincia = self.get_object(id)
        provincia.delete()

        return Response({"message": "La provincia a sido eliminada con exito"}, status=status.HTTP_204_NO_CONTENT)

class ListaComunasView(generics.ListCreateAPIView):

    parser_classes = [JSONParser]
    permission_classes = [AllowAny]
    queryset = Comuna.objects.all().order_by("nombre")
    serializer_class = ComunaSerializer
    pagination_class = PageNumberPagination

    def get(self, request, format=None):

        comunas = self.get_queryset()
        page = self.paginate_queryset(comunas)
        serializer = self.get_serializer(page, many=True)

        if not len(serializer.data):
            return Response({"message": "No hay comunas registradas"}, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):

        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response({"data": serializer.data, "message": "se creo la comuna con exito"}, status=status.HTTP_201_CREATED)

class DetalleProvinciaView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ComunaSerializer
    permission_classes = [AllowAny]

    def get_object(self, id:int):

        try:
            comuna = Comuna.objects.get(id_provincia = id)
        except Comuna.DoesNotExist:
            raise Http404

        return comuna
    
    def get(self, request, id:int, format=None):

        comuna = self.get_object(id)
        serializer = self.get_serializer(comuna)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id:int, fromat=None):

        comuna = self.get_object(id)
        serializer = self.get_serializer(comuna, data=request.data)

        if not serializer.is_valid():
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response({"data":serializer.data, "message": "Comuna actualizada con exito"}, status=status.HTTP_200_OK)
    
    def delete(self, request, id:int, format=None):

        comuna = self.get_object(id)
        comuna.delete()

        return Response({"message": "La comuna a sido eliminada con exito"}, status=status.HTTP_204_NO_CONTENT)