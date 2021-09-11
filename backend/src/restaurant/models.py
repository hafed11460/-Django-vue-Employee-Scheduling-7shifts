from django.db import models
from django.utils.translation import ugettext_lazy as _




class Restaurant(models.Model):
    name =  models.CharField(_("name"), max_length=50)

    def __str__(self):
        return self.name



class Location(models.Model):
    name = models.CharField(_("location name"), max_length=50)
    restaurant   =  models.ForeignKey(Restaurant,related_name='locations', verbose_name=_("rastaurant"), on_delete=models.CASCADE)
    # manager = models.ForeignKey(Employee, verbose_name=_("manager"), on_delete=models.CASCADE ,limit_choices_to={'employee_type': 5})

    def __str__(self):
        return f'{self.restaurant} - {self.name}'
