from restaurant.models import Restaurant
from restaurant.api.serializer import AllRestaurantSerializer, RestaurantSerializer
from django.utils.translation import gettext_lazy as _
from django.db.models import Q

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView,
)


class RastaurantListAPIView(ListAPIView):
    # permission_classes = [IsAuthenticated ]
    serializer_class = AllRestaurantSerializer
    # filter_backends = (DjangoFilterBackend,)

    queryset = Restaurant.objects.all()
    # def get_queryset(self):
    #     # user = self.request.user
    #     # return Offer.objects.filter(buyer=user,is_active=True,is_deleted=False).order_by('-created_at')
    #     return Shift.objects.filter()
