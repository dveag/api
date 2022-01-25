import uuid

from django.db import models


class Base(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Nft(Base):
    id = models.BigAutoField(primary_key=True)
    creator_network = models.UUIDField(unique=True, default=uuid.uuid4)
    creator_wallet_id = models.UUIDField(unique=True)


class Item(Base):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    creator = models.ForeignKey(Nft, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    external_link = models.CharField(max_length=1000)
    collection = models.UUIDField(unique=True, null=True)
    supply = models.IntegerField(default=1)
    royalties = models.DecimalField(null=True, max_digits=10, decimal_places=2)

