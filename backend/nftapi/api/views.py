from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.core.exceptions import ObjectDoesNotExist

from api.models import Nft
from api.serializers import (
    ItemSerializer,
    NftCreateSerializer,
    NftSerializer,
)
from api.services import NftService



@api_view(['POST'])
def nft_mint(request):
    serializer = NftCreateSerializer(data=request.data)
    serializer.is_valid()
    try:
        NftService.create_nft_items(serializer.validated_data)
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def nft_details(request, pk=None):
    try:
        item = NftService.get_item(pk)
        item_serializer = ItemSerializer(item)
        nft_serializer = NftSerializer(item.nft)
        nft_data = nft_serializer.data
        nft_data['assets'] = [item_serializer.data]
        return Response({'data': nft_data}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'data': 'NFT does not exist with asset id %s' % pk }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def nft_list(request):
    try:
        nft_query = NftService.list_nft()
        serializer = NftCreateSerializer(nft_query, many=True)
        return Response(serializer.data)
    except:
        return Response({'data': 'Unexpected error' }, status=status.HTTP_400_BAD_REQUEST)
