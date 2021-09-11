from restaurant.models import Location, Restaurant
from rest_framework.serializers import ModelSerializer,SerializerMethodField


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id','name']


class LocationSerializer(ModelSerializer):
    restaurant = RestaurantSerializer(many=False, read_only=True)
    class Meta:
        model = Location
        fields = ['id','name','restaurant']





#### use this for home page
class AllLocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ['id','name']

class AllRestaurantSerializer(ModelSerializer):
    location =  SerializerMethodField()
    class Meta:
        model = Restaurant
        fields = ['id','name','location']
    def get_location(self,obj):
        results = Location.objects.filter(restaurant__id=obj.id)
        return AllLocationSerializer(results, many=True).data