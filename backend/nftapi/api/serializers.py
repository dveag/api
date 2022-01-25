from rest_framework import serializers
from .models import Nft, Item


class NftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nft
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'description', 'external_link', 'collection', 'supply', 'royalties']


class NftCreateSerializer(NftSerializer):
    assets = ItemSerializer(many=True, source='items')
