from shift.api.views import CreateShiftAPIView, DestroyShiftAPIView, ListShiftAPIView, ShiftsChoicesAPIView, UpdateShiftAPIView
from django.urls import path
from employee.api.views import *


app_name = 'api-shift'
urlpatterns = [

    path('',ListShiftAPIView.as_view(), name='shifts-list') ,
    path('create/',CreateShiftAPIView.as_view(), name='shifts-create') ,
    path('<int:pk>/update/',UpdateShiftAPIView.as_view(), name='shifts-update') ,
    path('<int:pk>/delete/',DestroyShiftAPIView.as_view(), name='shifts-delete') ,

    path('choices/',ShiftsChoicesAPIView.as_view(), name='shifts-choices') ,
]