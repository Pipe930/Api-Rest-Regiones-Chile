from rest_framework import serializers
from .models import Region, Comuna, Provincia

class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = ("nombre", "sigla", "poblacion", "superficie", "capital", "numero_region")
    
    def create(self, validated_data):

        region = Region.objects.create(**validated_data)

        return region
    
    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.sigla = validated_data.get('sigla', instance.sigla)
        instance.poblacion = validated_data.get('poblacion', instance.poblacion)
        instance.superficie = validated_data.get('superficie', instance.superficie)
        instance.capital = validated_data.get('capital', instance.capital)
        instance.numero_region = validated_data.get('numero_region', instance.numero_region)

        instance.save()

        return instance

class ProvinciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provincia
        fields = ("nombre", "id_region")

    def create(self, validated_data):
        provincia = Provincia.objects.create(**validated_data)
        return provincia
    
    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.id_region = validated_data.get('id_region', instance.id_region)

        instance.save()
        return instance

class ComunaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comuna
        fields = ("nombre", "id_provincia")

    def create(self, validated_data):
        comuna = Comuna.objects.create(**validated_data)
        return comuna
    
    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.id_provincia = validated_data.get('id_provincia', instance.id_provincia)

        instance.save()
        return instance