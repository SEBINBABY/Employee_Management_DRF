from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


# Custom Pagination class for Employee
class EmployeePagination(PageNumberPagination):
    page_size = 10


# List of employees/ create a new employee
class EmployeeList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = EmployeePagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['department', 'role']

    def get(self, request):
        employees = Employee.objects.all()
        # Manually apply filters
        for backend in list(self.filter_backends):
            employees = backend().filter_queryset(request, employees, self)
        # Manually apply pagination
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(employees, request)
        emp_serializer = EmployeeSerializer(result_page, many=True)
        return Response({
            "message": "success",
            "data": emp_serializer.data,
            "status": status.HTTP_200_OK
        })

    def post(self, request):
        if request.data:
            emp_serializer = EmployeeSerializer(data=request.data)
            if emp_serializer.is_valid():
                emp_serializer.save()
                return Response({
                    "message": "success",
                    "data": emp_serializer.data,
                    "status": status.HTTP_201_CREATED
                })
            else:
                return Response({
                    "message": "Invalid data",
                    "errors": emp_serializer.errors,
                    "status": status.HTTP_400_BAD_REQUEST
                })
        else:
            return Response({
                "message": "Failed",
                "data": {},
                "status": status.HTTP_204_NO_CONTENT
            })


# Retrieve details/update a specific employee/ delete a specific employee
class EmployeeDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            employee = Employee.objects.get(id=id)
            return employee
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, id):
        employee = self.get_object(id)
        emp_serializer = EmployeeSerializer(employee)
        return Response({
            "message": "Success",
            "data": emp_serializer.data,
            "status": status.HTTP_200_OK
        })

    def put(self,request, id):
        employee = self.get_object(id)
        emp_serializer = EmployeeSerializer(employee, data=request.data)
        if emp_serializer.is_valid():
            emp_serializer.save()
            return Response({
                "message": "success",
                "data": emp_serializer.data,
                "status": status.HTTP_201_CREATED
            })
        else:
            return Response({
                "message": "Invalid data",
                "errors": emp_serializer.errors,
                "status": status.HTTP_400_BAD_REQUEST
            })

    def delete(self, request, id):
        employee = self.get_object(id)
        employee.delete()
        return Response({
            "message": "Data deleted successfully",
            "status": status.HTTP_204_NO_CONTENT
        })


# For creating the token automatically whenever a user is saved
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)









