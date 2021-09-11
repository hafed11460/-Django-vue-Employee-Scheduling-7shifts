from employee.api.permissions import IsManager
from shift.api.serializer import CreateShiftsSerializer, ShiftsSerializer
from shift.models import Shift
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

class ShiftsChoicesAPIView(APIView):
    permission_classes = [IsAuthenticated ]
    def get(self, request, format=None):
        context = {}
        context['JOB_TYPE_CHOICES']  = Shift.JOB_TYPE_CHOICES
        return Response(context)

class ListShiftAPIView(ListAPIView):
    permission_classes = [IsAuthenticated,IsManager ]
    serializer_class = ShiftsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = {
        'date':['exact'],
        }
    queryset = Shift.objects.all()




class CreateShiftAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated,IsManager ]
    serializer_class = CreateShiftsSerializer
    queryset = Shift.objects.all()
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        serializer = CreateShiftsSerializer( data=request.data)
        if serializer.is_valid():
            employee = request.data['employee']
            date  = request.data['date']
            startHour = serializer.validated_data.get('starthour')
            endHour = serializer.validated_data.get('endhour')
            q = (
                  Q(employee=employee ,date=date)
                & (Q(starthour__range=(startHour,endHour)) | Q(endhour__range=(startHour,endHour)))
                )
            print(q)
            shift =  Shift.objects.filter(q).first()

            if shift:
                old_shift = ShiftsSerializer(shift)
                context = {}
                context['message'] = _('range of this shift is existe ')
                context['data']= old_shift.data
                return Response(context, status=status.HTTP_404_NOT_FOUND)
            shift_created =  serializer.save()
            curent_shift = Shift.objects.get(id=shift_created.id)

            curent_shift_serializer =   ShiftsSerializer(curent_shift)
            return Response(curent_shift_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)



class UpdateShiftAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated,IsManager ]
    serializer_class = ShiftsSerializer
    queryset = Shift.objects.all()

    def put(self, request, *args, **kwargs):

        serializer = CreateShiftsSerializer( data=request.data)
        if serializer.is_valid():
            employee = request.data['employee']
            date  = request.data['date']
            startHour = serializer.validated_data.get('starthour')
            endHour = serializer.validated_data.get('endhour')
            q = (
                Q(employee=employee ,date=date)
                 & ~Q(id=self.get_object().id)
                & (Q(starthour__range=(startHour,endHour)) | Q(endhour__range=(startHour,endHour)))
                )
            print(q)
            shift =  Shift.objects.filter(q).first()

            if shift:
                old_shift = ShiftsSerializer(shift)
                context = {}
                context['message'] = _('range of this shift is existe ')
                context['data']= old_shift.data
                return Response(context, status=status.HTTP_404_NOT_FOUND)
            # shift_created =  serializer.save()
            # curent_shift = Shift.objects.get(id=shift_created.id)
            self.update(request, *args, **kwargs)
            curent_shift_serializer =   ShiftsSerializer(self.get_object())
            return Response(curent_shift_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class DestroyShiftAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated,IsManager ]
    serializer_class = ShiftsSerializer
    queryset = Shift.objects.all()