# Generated by Django 4.0 on 2022-01-25 21:28

import uuid
from decimal import Decimal

from django.db import migrations


def create_initial_data(apps, schema_editor):
    Nft = apps.get_model('api', 'Nft')
    Item = apps.get_model('api', 'Item')
    nft = Nft.objects.create(
        creator_network=uuid.uuid4(), 
        creator_wallet_id=uuid.uuid4()
    )
    items = [ ]
    for i in range(5):
        data = {
            'id': uuid.uuid4(),
            'name': 'test %s' % i,
            'description': 'description %s' % i,
            'external_link': 'http://none',
            'collection': uuid.uuid4(),
            'supply': i,
            'royalties': Decimal('{}.0{}'.format(i, i)),
            'nft': nft
        }
        item = Item(**data)
        items.append(item)

    Item.objects.bulk_create(items)

    User = apps.get_model('auth', 'User')
    User.objects.create_superuser('admin', 'admin@admin.com', 'admin')


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_item_nft'),
    ]

    operations = [
        migrations.RunPython(create_initial_data)
    ]
