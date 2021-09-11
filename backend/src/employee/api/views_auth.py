


from employee.api.serializer import EmployeeSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from employee.models import Employee
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import ugettext_lazy as _


# class RegisterView(APIView):
#     def post(self,request):
#         serializer = AccountRegisterSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


class LoginView(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']

        if not email:
            return  Response({"email": [_("email does not exist.")]}, status=status.HTTP_400_BAD_REQUEST)

        user = Employee.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed(_('User not found'))

        if not user.check_password(password):
            raise AuthenticationFailed(_('Incorrect password'))


        refresh = RefreshToken.for_user(user)

        return Response ({
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        })


class CurrentLoggedInUser(ModelViewSet):
    queryset = Employee.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = EmployeeSerializer

    def retrieve(self, request, *args, **kwargs):
        user= self.queryset.get(email=request.user.email)
        serializer = self.get_serializer(user)
        # role = user.role
        # role_name = 'Manager' if  (role.name == 'Manager' or role.name == 'Admin' ) else 'User'
        # user = {
        #     'id':user.id,
        #     'first_name':user.first_name,
        #     'last_name':user.last_name,
        #     'email':user.email,
        #     'is_active':user.is_active,
        #     'role': role_name,
        #     'role_id': role.id,
        #     'location':user.location.name,
        #     'profile_image':user.profile_image.url,
        # }
        # return Response({'user': user})
        return Response({'user': serializer.data})

#  "id": 3,
        # "email": "hafed@gmail.com",
        # "first_name": "Hafed",
        # "last_name": "Tabet",
        # "profile_image": "http://localhost:8000/media/profile_images/3/profile_image.png",
        # "is_active": true,
        # "location": {
        #     "id": 1,
        #     "name": "Location A",
        #     "restaurant": {
        #         "id": 1,
        #         "name": "restaurant A"
        #     }
        # },
        # "role": {
        #     "id": 3,
        #     "name": "front desk"
        # }
class logout_view(APIView):
    def get(self, request):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
