from django.urls import path
from .views import EmployeeList, EmployeeDetail
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # API Endpoints - GET/POST
    path('api/employees/', EmployeeList.as_view(), name='employees_list'),
    # API Endpoints - PUT/DELETE
    path('api/employees/<int:id>/', EmployeeDetail.as_view(), name='employee_detail'),
    # API endpoint to get Token
    path('api-token-auth/', obtain_auth_token, name="api_token_auth"),
]