from employee.api.serializer import  EmployeeShiftSerializer
from employee.models import Employee
from shift.models import Shift
from rest_framework.serializers import ModelSerializer


class ShiftsSerializer(ModelSerializer):
    employee = EmployeeShiftSerializer(many=False, read_only=True)
    class Meta:
        model = Shift
        fields = ['location','id','job','note','starthour','endhour','date','employee']


class CreateShiftsSerializer(ModelSerializer):
    class Meta:
        model = Shift
        fields = ['location','job','note','starthour','endhour','date','employee']
