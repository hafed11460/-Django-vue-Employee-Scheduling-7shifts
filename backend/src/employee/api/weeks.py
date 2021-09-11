from employee.api.permissions import IsManager, OwnerOrEmployeePermission
from employee.models import Employee
from datetime import datetime,timedelta
from shift.models import Shift

from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class CopyWeekAPIView(APIView):
    permission_classes = [IsAuthenticated,IsManager,OwnerOrEmployeePermission]
    def get(self, request, format=None):
        date = request.GET.get('date', '')
        if not date:
            date =datetime.today().strftime('%Y-%m-%d')
        days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

        startDate = (datetime.strptime(date, '%Y-%m-%d') + timedelta(days=7)).strftime('%Y-%m-%d')
        endDate = (datetime.strptime(date, '%Y-%m-%d') + timedelta(days=(7+6))).strftime('%Y-%m-%d')

        context ={}
        shiftsOfNexWeek = Shift.objects.filter(date__range=[startDate,endDate])
        if not shiftsOfNexWeek:
            for idx, dayName in enumerate(days):
                currentDate = (datetime.strptime(date, '%Y-%m-%d') + timedelta(days=idx)).strftime('%Y-%m-%d')
                nextWeekDate = (datetime.strptime(date, '%Y-%m-%d') + timedelta(days=(idx+7))).strftime('%Y-%m-%d')

                employees = Employee.objects.filter(is_admin=False,is_active=True)
                for employee in employees:
                    shifts = employee.shifts.filter(date=currentDate)
                    for shift in shifts:
                        newShift = Shift.objects.get(pk=shift.pk)
                        newShift.date = datetime.strptime(nextWeekDate, '%Y-%m-%d')
                        newShift.id = None
                        newShift.save()

            context['message'] = 'copied successfull'
            return Response(context, status=status.HTTP_200_OK)
        else:
            context['message'] = 'cannot copy this week to next week because the next week is not empty'
            return Response(context, status=status.HTTP_404_NOT_FOUND)

def copy_week(date):


    return True



class CleareWeekAPIView(APIView):
    permission_classes = [IsAuthenticated,IsManager,OwnerOrEmployeePermission]
    def get(self, request, format=None):
        date = request.GET.get('date', '')
        if not date:
            date =datetime.today().strftime('%Y-%m-%d')

        cleare_week(date)
        context ={}
        context['message'] = 'copied successfull'
        return Response(context)


def cleare_week(date):
    days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    for idx, dayName in enumerate(days):
        currentDate = (datetime.strptime(date, '%Y-%m-%d') + timedelta(days=idx)).strftime('%Y-%m-%d')
        # nextWeekDate = (datetime.strptime(date, '%Y-%m-%d') + timedelta(days=(idx+7))).strftime('%Y-%m-%d')

        employees = Employee.objects.filter(is_admin=False,is_active=True)
        for employee in employees:
            shifts = employee.shifts.filter(date=currentDate)
            for shift in shifts:
                shift.delete()
    context ={}
    context['message'] = 'Week cleared successfull'
    return Response(context)