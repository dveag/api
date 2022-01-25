from rest_framework import serializers
from .models import Nft, Item


class NftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nft
        fields = '__all__'


class ItemSerializer(serializers.Serializer):
    class Meta:
        model = Item
        fields = '__all__'

