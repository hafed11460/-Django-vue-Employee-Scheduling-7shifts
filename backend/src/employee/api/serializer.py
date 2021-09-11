from restaurant.api.serializer import LocationSerializer
from shift.models import Shift
from employee.models import Employee, Role
from rest_framework.serializers import ModelSerializer,SerializerMethodField
from datetime import datetime,timedelta

class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = ['id','name']


class ShiftsSerializer(ModelSerializer):
    job = RoleSerializer(many=False, read_only=True)
    class Meta:
        model = Shift
        fields = ['id','job','note','starthour','endhour','date','job']


class EmployeeShiftSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id',)


class UpdateEmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id','email','first_name', 'last_name',)

class DisableEmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('is_active',)



class CreateEmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id','email', 'password', 'first_name', 'last_name','profile_image','is_active','location','role')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8},
        }
    def create(self , validated_data):
            email = validated_data.pop('email',None)
            password = validated_data.pop('password',None)
            email=email.lower()
            instance = self.Meta.model(**validated_data)
            instance.email = email
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance

class EmployeeSerializer(ModelSerializer):
    location = LocationSerializer(many=False, read_only=True)
    role = LocationSerializer(many=False, read_only=True)
    class Meta:
        model = Employee
        fields = ('id','email', 'password', 'first_name', 'last_name','profile_image','is_active','location','role')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8},
        }


class EmployeeFilterSerializer(ModelSerializer):
    shifts = SerializerMethodField()
    location = LocationSerializer(many=False, read_only=True)
    class Meta:
        model = Employee
        fields = ('id','email', 'password', 'first_name', 'last_name','profile_image' ,'shifts','is_active','role','location')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8},
        }

    def get_shifts(self, obj):
        request =  self.context['request']
        date = request.GET.get('date', '')
        if date:
            results = Shift.objects.filter(employee__id=obj.id, date=date)
        else:
            date = datetime.today().strftime('%Y-%m-%d')
            results = Shift.objects.filter(employee__id=obj.id,date=date)
        return ShiftsSerializer(results, many=True).data


class EmployeeWeekFilterSerializer(ModelSerializer):
    shifts = SerializerMethodField()

    class Meta:
        model = Employee
        fields = ('id','email', 'password', 'first_name', 'last_name','profile_image' ,'shifts',)
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8},
        }

    def get_shifts(self, obj):
        request =  self.context['request']
        date = request.GET.get('date', '')
        now = datetime.now()
        monday = now - timedelta(days = now.weekday())
        # print(monday)
        if not date:
            date = datetime.today().strftime('%Y-%m-%d')
            date = (datetime.strptime(date, '%Y-%m-%d') + timedelta(days=0)).strftime('%Y-%m-%d')
            results = Shift.objects.filter(employee__id=obj.id, date=date).order_by('starthour')
            # print(date)

        # startDay = (datetime.strptime(date, '%Y-%m-%d') + timedelta(days=0)).strftime('%Y-%m-%d')
        endDate = (datetime.strptime(date, '%Y-%m-%d') + timedelta(days=6)).strftime('%Y-%m-%d')

        results = Shift.objects.filter(employee__id=obj.id,date__range=[date, endDate]).order_by('starthour')
        return ShiftsSerializer(results, many=True).data
