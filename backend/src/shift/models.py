from restaurant.models import Location
from employee.models import Employee, Role
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Shift(models.Model):

    JOB_TYPE_CHOICES = (
      (1, _('manager')),
      (2, _('cashier')),
      (3, _('front desk')),
    )

    location   =  models.ForeignKey(Location, verbose_name=_("location"), on_delete=models.CASCADE)
    employee   =  models.ForeignKey(Employee,related_name='shifts', verbose_name=_("employee"), on_delete=models.CASCADE)
    starthour  =  models.TimeField(_('start hour '))
    endhour    =  models.TimeField(_('end hour'))
    date       =  models.DateField(_("date"),  auto_now_add=False)
    job        =  models.ForeignKey(Role, verbose_name=_("role"), on_delete=models.CASCADE)
    # job        =  models.PositiveSmallIntegerField(choices=JOB_TYPE_CHOICES)
    note       =  models.TextField(_("note") ,null=True, blank=True)

    def __str__(self):
        return f'{self.employee.id} - {self.employee.first_name}'