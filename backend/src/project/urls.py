
# from core.api.views import OffersListView
from employee.api.views_auth import CurrentLoggedInUser, LoginView, logout_view
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # path('core/', include('core.api.urls')),
    path('employees/', include('employee.api.urls')),
    path('shifts/', include('shift.api.urls')),
    path('restaurants/', include('restaurant.api.urls')),


    # path('offers/',OffersListView.as_view(), name='offers') ,

    ### Authentification
    path('login/',LoginView.as_view(), name='login') ,
    path('logout/',logout_view, name='logout') ,
    # path('register/',RegisterView.as_view(), name='login') ,
    path('user/', CurrentLoggedInUser.as_view({'get': 'retrieve'}), name="current_user"),

    # path('login/',obtain_auth_token, name='login') ,
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
