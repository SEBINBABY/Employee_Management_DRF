from django.db import models


# Employee Model
class Employee(models.Model):
    DEPARTMENT_CHOICES = [
                            ("HR", "HR"),
                            ("Engineering", "Engineering"),
                            ("Sales", "Sales")
                          ]
    ROLE_CHOICES = [
                    ("Manager", "Manager"),
                    ("Developer", "Developer"),
                    ("Analyst", "Analyst")
                    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, null=True, blank=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, null=True, blank=True)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


