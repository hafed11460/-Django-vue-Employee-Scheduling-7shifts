

# from core.models import Offer, Tests
# from core.api.serializers import OfferSerializer, TestSerializer
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.generics import (
#     ListAPIView,
#     CreateAPIView
# )
# class OffersListView(ListAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = OfferSerializer

#     # # search_fields = ['title', 'description']
#     queryset = Offer.objects.all()

# class TestCreateAPIView(CreateAPIView):
#     # permission_classes = [IsAuthenticated]
#     serializer_class = TestSerializer

#     # # search_fields = ['title', 'description']
#     queryset = Tests.objects.all()