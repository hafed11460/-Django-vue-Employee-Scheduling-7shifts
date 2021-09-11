from restaurant.api.views import RastaurantListAPIView
from django.urls import path


app_name = 'api-restaurant'
urlpatterns = [

    path('',RastaurantListAPIView.as_view(), name='Restaurant-list') ,
    # path('create/',CreateShiftAPIView.as_view(), name='shifts-create') ,
    # path('<int:pk>/update/',UpdateShiftAPIView.as_view(), name='shifts-update') ,
    # path('<int:pk>/delete/',DestroyShiftAPIView.as_view(), name='shifts-delete') ,

    # path('choices/',ShiftsChoicesAPIView.as_view(), name='shifts-choices') ,
]