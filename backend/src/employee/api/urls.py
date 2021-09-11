from employee.api.email import SendMail
from employee.api.weeks import CleareWeekAPIView, CopyWeekAPIView
from employee.api.csv import EmployeeCSVAPIView
from employee.api.excel import EmployeeExcelAPIView
from django.urls import path
from employee.api.views import *


app_name = 'api-employee'
urlpatterns = [

    path('',ListEmployeesAPIView.as_view(), name='employee-list') ,
    path('roles/',EmployeesRolesAPIView.as_view(), name='employee-roles') ,
    path('all/',AllEmployeesListAPIView.as_view(), name='employee-list') ,
    path('week/',ListEmployeesWeekAPIView.as_view(), name='employee-list') ,
    path('create/',CreateEmployeeAPIView.as_view(), name='employee-create') ,
    path('<int:pk>/',DetailEmployeeAPIView.as_view(), name='employee-detail') ,

    ## profile operation #####
    path('<int:pk>/profile/',EmployeeProfileAPIView.as_view(), name='employee-profile') ,
    path('<int:pk>/update/',UpdateEmployeeProfileAPIView.as_view(), name='employee-update') ,
    path('<int:pk>/disable/',DisableEmployeeProfileAPIView.as_view(), name='employee-disable') ,
    path('<int:pk>/delete/',DeleteEmployeeProfileAPIView.as_view(), name='employee-delete') ,


    path('<int:pk>/week/',DetailWeekEmployeeAPIView.as_view(), name='week-employee-detail') ,
    path('excel/',EmployeeExcelAPIView.as_view(), name='employee-excel') ,
    path('csv/',EmployeeCSVAPIView.as_view(), name='employee-csv') ,
    path('copy-week/',CopyWeekAPIView.as_view(), name='employee-copy-week') ,
    path('cleare-week/',CleareWeekAPIView.as_view(), name='employee-cleare-week') ,


    path('send-mail/',SendMail.as_view(), name='employee-send-mail') ,

    # this for employee not manager
    path('<int:pk>/simple-user/day/',UserEmployeeAPIView.as_view(), name='simple-employee') ,
    path('simple-user/week/',UserEmployeesWeekAPIView.as_view({'get': 'retrieve'}), name='simple-user-week') ,



    # path('<int:pk>/filter/',DetailEmployeeFilterAPIView.as_view(), name='employee-detail-filter') ,
    # path('offers/closed/',ListOfferClosedAPIView.as_view(), name='offers-closed') ,



]