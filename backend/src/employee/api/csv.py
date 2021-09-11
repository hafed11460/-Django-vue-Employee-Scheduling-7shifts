from employee.models import Employee
from rest_framework.views import APIView
from django.http import HttpResponse
from datetime import datetime,timedelta
import csv

class EmployeeCSVAPIView(APIView):

    def get(self, request, format=None):
        user = request.user
        date = request.GET.get('date', '')
        if not date:
             date = datetime.today().strftime('%Y-%m-%d')
             date = (datetime.strptime(date, '%Y-%m-%d') + timedelta(days=0)).strftime('%Y-%m-%d')
        response = createCSVFile(date,user)
        return response


def createCSVFile(date,user):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
    )
    # Employee ID Date First Last Location In Time Out Time Worked hours
    writer = csv.writer(response)
    writer.writerow(['Employee ID', 'Date', 'First', 'Last' ,'Location', 'In Time' , 'Out Time','Worked hours','Total'])

    days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    format = '%H:%M:%S'
    for idx, dayName in enumerate(days):
        currentDate = (datetime.strptime(date, '%Y-%m-%d') + timedelta(days=idx)).strftime('%Y-%m-%d')

        employees = Employee.objects.filter(is_admin=False,is_active=True,location=user.location.id)
        for employee in employees:

            shifts = employee.shifts.filter(date=currentDate)
            for shift in shifts:
                time = datetime.strptime(str(shift.endhour), format) - datetime.strptime(str(shift.starthour), format)
                # print(dir(time))
                writer.writerow([
                    employee.id,
                    currentDate,
                    employee.first_name,
                    employee.last_name,
                    employee.location.name,#location
                    shift.starthour,
                    shift.endhour,
                    time,
                     (time.total_seconds()/ (60*60))
                    ])
    return response