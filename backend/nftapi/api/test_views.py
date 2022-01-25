import unittest
import json
from uuid import uuid4
from decimal import Decimal

from django.urls import reverse
from django.test import Client

from api.models import Nft, Item


class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        nft = Nft.objects.create(
            creator_network=uuid4(), 
            creator_wallet_id=uuid4()
        )
        Item.objects.create(
            id=uuid4(),
            name='test 1',
            description='description 1',
            external_link='http://none',
            collection=uuid4(),
            supply=2,
            royalties=Decimal('100.04'),
            nft=nft
        )
        Item.objects.create(
            id=uuid4(),
            name='test 2',
            description='description 2',
            external_link='http://none',
            collection=uuid4(),
            supply=2,
            royalties=Decimal('0.04'),
            nft=nft
        )

    def test_list(self):
        response = self.client.get(reverse('nft-list'))
        self.assertEqual(response.status_code, 200)

    def test_get(self):
        last_item = Item.objects.last()
        url = reverse('nft-details', kwargs={'pk': last_item.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_wrong(self):
        url = reverse('nft-details', kwargs={'pk': str(uuid4())})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)

    def test_create(self):
        data = {
            'creator_wallet_id': str(uuid4()),
            'creator_network': str(uuid4()),
            'assets': [
                {
                    'id': str(uuid4()),
                    'name': 'tyyyy',
                    'description': 'xxxx',
                    'external_link': 'http://none',
                    'collection': str(uuid4()),
                    'supply': 1,
                    'royalties': 2.5
                }
            ]
        }
        url = reverse('nft-mint')
        response = self.client.post(
            url, 
            json.dumps(data), 
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
