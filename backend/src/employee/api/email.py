from employee.models import Employee
from django.core.mail import send_mail,EmailMessage
from employee.api.permissions import IsManager, OwnerOrEmployeePermission
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import csv
from datetime import datetime,timedelta
from django.http import HttpResponse


class SendMail(APIView):
    permission_classes = [IsAuthenticated,IsManager,OwnerOrEmployeePermission]
    def post(self,request):
        user = request.user
        date = request.GET.get('date', '')
        # startDate = request.data.get('startdate', '')
        # endDate = request.data.get('enddate', '')
        # print('----------------------------------')
        # print(startDate, endDate)
        # print('----------------------------------')
        if not date:
            date = datetime.today().strftime('%Y-%m-%d')
            date = (datetime.strptime(date, '%Y-%m-%d') + timedelta(days=0)).strftime('%Y-%m-%d')
        context ={}

        subject = request.data.get('subject','')
        message = request.data.get('message','')
        print(date)
        # csvFile = createCSVFile(date,user)
        # mailList = getMailList(user)
        # message = EmailMessage(
        #     subject,
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     mailList
        # )
        # message.attach('shifts.csv', csvFile.getvalue(), 'text/csv')
        # message.send()
        context['success'] = 'All email are send successfull'
        return Response(context)


def getMailList(user):
    mailList = []
    employees = Employee.objects.filter(is_admin=False,is_active=True,location=user.location.id).exclude(id=user.id)
    for employee in employees:
        mailList.append(employee.email)
    return mailList


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

        employees = Employee.objects.filter(is_admin=False,is_active=True,location=user.location.id).exclude(id=user.id)
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