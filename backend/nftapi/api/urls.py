from django.urls import path, include
from api import views


urlpatterns = [
    path('v1/mint', views.nft_mint),
    path('v1/NFT/<uuid:pk>', views.nft_details),
    path('v1/NFT/all', views.nft_list),
]