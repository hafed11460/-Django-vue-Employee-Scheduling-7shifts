
import django_filters
from django.db.models import Q
from shift.models import Shift



class DateShifFilter(django_filters.FilterSet):
    date = django_filters.IsoDateTimeFilter()
    class Meta:
        model = Shift
        fields = ['date']



# class CustomOfferFilter(django_filters.FilterSet):
#     time_length = django_filters.MultipleChoiceFilter(method='my_custom_filter')
#     max_proposals = django_filters.MultipleChoiceFilter(method='my_custom_filter')
#     created_at = django_filters.IsoDateTimeFilter()
#     # q = django_filters.CharFilter(method='my_custom_filter',label="Search")

#     class Meta:
#         model = Offer
#         fields = ['time_length','max_proposals','created_at']
#         # fields = {
        #     'time_length':['in'],
        #     'max_proposals':['in']
        # }

    # def my_custom_filter(self, queryset, name, value):
    #     return Location.objects.filter(
    #         Q(loc__icontains=value) | Q(loc_mansioned__icontains=value) | Q(loc_country__icontains=value) | Q(loc_modern__icontains=value)
    #     )
    # def my_custom_filter(self, queryset, name, value):

    #     return queryset.filter(
    #         Q(time_length__in=[2,3]) #or Q(max_proposals__in=[1]) #| Q(loc_country__icontains=value) | Q(loc_modern__icontains=value)
    #     )
    # def filter_time_length(self, queryset, name, value):
        # print('------------------------------------------------------')
        # print(name, value)
        # print('------------------------------------------------------')
        # return Offer.objects.filter(
        #     Q(time_length__in=value) #| Q(loc_mansioned__icontains=value) | Q(loc_country__icontains=value) | Q(loc_modern__icontains=value)
        # )

    # def filter_max_proposals(self, queryset, name, value):
    #      return Offer.objects.filter(
    #         Q(max_proposals__in=value) #| Q(loc_mansioned__icontains=value) | Q(loc_country__icontains=value) | Q(loc_modern__icontains=value)
    #     )