from shift.models import Shift
from employee.api.serializer import EmployeeSerializer
from django.http.response import FileResponse
from employee.models import Employee
from rest_framework.views import APIView
from django.http import HttpResponse
import xlsxwriter
import io
from datetime import datetime,timedelta


class EmployeeExcelAPIView(APIView):

    def get(self, request, format=None):
        date = request.GET.get('date', '')
        if not date:
            date =datetime.today().strftime('%Y-%m-%d')
        response = HttpResponse(content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename=your_template_name.xlsx'
        excel_file = createExcelFile(date)
        response.write(excel_file)
        return response



def createExcelFile(date):
    # employees = Employee.objects.all()
    output      = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    sheetColor = ['#A52A2A','#7FFF00','#6495ED','#00FFFF','#B8860B','#006400','#483D8B']

    for idx, dayName in enumerate(days):
        currentDate = (datetime.strptime(date, '%Y-%m-%d') + timedelta(days=idx)).strftime('%Y-%m-%d')
        worksheet = workbook.add_worksheet(dayName)
        worksheet.set_tab_color(sheetColor[idx])
        # worksheet.autofilter('A1:D51')


        worksheet.set_default_row(20)
        #########################################################
        # worksheet Headers
        #########################################################
        merge_format = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': '#F5DEB3'})


        headerCell = workbook.add_format({
            'bold': 1,
            # 'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': '#F5F5F5'})

        employeeCell = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': '#F5F5F5'})

        hourCell = workbook.add_format({
            # 'bold': 1,
            # 'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            # 'fg_color': '#F5F5F5'
            })



        # Merge 3 cells.
        worksheet.merge_range('A1:A3', dayName, merge_format)
        worksheet.merge_range('B1:B3', currentDate, merge_format)
        # Set the autofilter.
        worksheet.autofilter('B4:T4')

        bold = workbook.add_format({'bold': True,'bg_color': '#F5F5F5'})
        success = workbook.add_format({'bg_color': '#9ACD32'})

        row = 4
        col = 0
        ## start  header ##########
        # set width cell
        worksheet.set_column(0, 0, 25)


        worksheet.write(3, col, 'Employee Name',headerCell)
        col = 1

        for hour in Shift.HOUR_TYPE_CHOICES:
            print(hour)
            worksheet.write(3,col,str(hour[1]) ,headerCell)
            col += 1

        # set column width
        worksheet.set_column(1, col, 10)
        # worksheet.set_column(0, col, secondary)
        sickIndex = col
        totalIndex = col+1
        worksheet.write(3, sickIndex, 'Sick' , bold )

        totalIndex = col+1
        worksheet.write(3, totalIndex, 'Total' , bold )
        ## end header ############


        col = 0
        row = 4
        employees = Employee.objects.filter(is_admin=False,is_active=True)
        for employee in employees:

            shift = employee.shifts.filter(date=currentDate).first()
            total = 0
            if shift  :
                startHour = shift.starthour
                endHour = shift.endhour
                job = Shift.JOB_TYPE_CHOICES[shift.job-1][1]
                total = endHour - startHour
                for i in range(startHour,endHour):
                    worksheet.write(row, col+i,str(job) ,hourCell)
            else:
                 worksheet.write(row, sickIndex, 'sick' , hourCell )


            # set cell hight
            worksheet.set_row(row, 30)
            worksheet.write(row, col, employee.first_name + ' ' + employee.last_name,employeeCell)
            worksheet.write(row, totalIndex, total)

            row +=1
            col = 0

    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data