from django.db import transaction

from api.models import Nft, Item

class NftService:

    @staticmethod
    @transaction.atomic
    def create_nft_items(validated_data):
        items = validated_data.pop('items')
        nft = Nft.objects.create(**validated_data)
        items_instances = [Item(nft=nft, **item) for item in items]
        Item.objects.bulk_create(items_instances)
    
    @staticmethod
    def get_item(pk):
        return Item.objects.select_related('nft').get(pk=pk)

    @staticmethod
    def list_nft():
        return Nft.objects.prefetch_related('items').all().order_by('created_on')



