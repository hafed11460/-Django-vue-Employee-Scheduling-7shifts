from employee.api.permissions import IsManager, OwnerOrEmployeePermission
from employee.models import Employee, Role

from employee.api.serializer import CreateEmployeeSerializer, DisableEmployeeSerializer, EmployeeFilterSerializer, EmployeeSerializer, EmployeeWeekFilterSerializer, RoleSerializer, UpdateEmployeeSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView,
)



# ########### this for  to manage All employees [ actove or descative employee]
class AllEmployeesListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated ]
    serializer_class = EmployeeFilterSerializer
    def get_queryset(self):
        user = self.request.user
        # return Employee.objects.filter(is_admin=False)
        return Employee.objects.filter(is_admin=False,location=user.location)



class EmployeesRolesAPIView(ListAPIView):
    # permission_classes = [IsAuthenticated,IsManager,OwnerOrEmployeePermission]
    serializer_class = RoleSerializer
    filter_backends = (DjangoFilterBackend,)
    def get_queryset(self):
        return  Role.objects.exclude(name='Manager')


class ListEmployeesAPIView(ListAPIView):
    permission_classes = [IsAuthenticated,IsManager,OwnerOrEmployeePermission]
    serializer_class = EmployeeFilterSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = {
        'shifts__date':['exact'],
        }
    def get_queryset(self):
        user = self.request.user
        return Employee.objects.filter(is_admin=False,is_active=True,location=user.location)



class CreateEmployeeAPIView(APIView):
    permission_classes = [IsAuthenticated,IsManager,OwnerOrEmployeePermission]
    def post(self,request):
        serializer = CreateEmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class DetailEmployeeAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated,IsManager,OwnerOrEmployeePermission]
    serializer_class = EmployeeFilterSerializer
    def get_queryset(self):
        user = self.request.user
        return Employee.objects.filter(is_admin=False,location=user.location)




###################################################
########### Simple  Employee  ######################
###################################################

class UserEmployeeAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeFilterSerializer
    def get_queryset(self):
        user = self.request.user
        return Employee.objects.filter(is_admin=False,id=user.id)


# class UserEmployeesWeekAPIView(ListAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = EmployeeWeekFilterSerializer
#     filter_backends = (DjangoFilterBackend,)
#     def get_queryset(self):
#         user = self.request.user
#         return Employee.objects.filter(is_admin=False,is_active=True ,id=user.id)


class UserEmployeesWeekAPIView(ModelViewSet):
    queryset = Employee.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = EmployeeWeekFilterSerializer

    def retrieve(self, request, *args, **kwargs):
        user_profile = self.queryset.get(id=request.user.id)
        serializer = self.get_serializer(user_profile)
        # user = {
        #     'first_name':empl.first_name,
        #     'last_name':empl.last_name,
        #     'email':empl.email,
        #     'role':empl.role.name,
        #     'location':empl.location.name,
        #     'profile_image':empl.profile_image.url,
        # }
        return Response({'user': serializer.data})


###################################################
########### Employee Profile ######################
###################################################

# Uses this class fo show employee profile
class EmployeeProfileAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated,IsManager,OwnerOrEmployeePermission]
    serializer_class = EmployeeSerializer
    def get_queryset(self):
        return Employee.objects.filter(is_admin=False)

# Use this class to update profile of employee
class UpdateEmployeeProfileAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,IsManager,OwnerOrEmployeePermission)
    serializer_class = UpdateEmployeeSerializer
    queryset = Employee.objects.all()


class DisableEmployeeProfileAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,IsManager,OwnerOrEmployeePermission)
    serializer_class = DisableEmployeeSerializer
    queryset = Employee.objects.all()


class DeleteEmployeeProfileAPIView(DestroyAPIView):
    permission_classes = (IsAuthenticated,IsManager,OwnerOrEmployeePermission)
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()







###################################################
########### Employee Week shedule  ################
###################################################

class ListEmployeesWeekAPIView(ListAPIView):
    permission_classes = [IsAuthenticated,IsManager]
    serializer_class = EmployeeWeekFilterSerializer
    filter_backends = (DjangoFilterBackend,)
    def get_queryset(self):
        user = self.request.user
        return Employee.objects.filter(is_admin=False,is_active=True ,location=user.location)


class DetailWeekEmployeeAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated,IsManager]
    serializer_class = EmployeeWeekFilterSerializer
    def get_queryset(self):
        user = self.request.user
        return Employee.objects.filter(is_admin=False,location=user.location)
