from rest_framework import serializers


class ItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=1000)
    external_link = serializers.URLField()
    collection = serializers.CharField()
    supply = serializers.IntegerField()
    royalties = serializers.DecimalField()


class NftSerializer(serializers.Serializer):
    network = serializers.UUIDField(required=True)
    wallet_id = serializers.UUIDField(required=True)