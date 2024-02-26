from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from datetime import datetime
class StateMaster(models.Model):
    state_name = models.CharField(max_length=200)
    state_code = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=datetime.today())
    updated_date = models.DateTimeField(default=datetime.today())
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.state_name
    

class UserMaster(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    phone = models.BigIntegerField()
    city = models.CharField(max_length=200)
    gender = models.CharField(max_length=20)
    joining_date = models.DateField()
    state = models.ForeignKey(StateMaster,on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.today())
    updated_date = models.DateTimeField(default=datetime.today())
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class TaskMaster(models.Model):
    task_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    assign_date= models.DateField()
    state = models.ForeignKey(StateMaster,on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.today())
    updated_date = models.DateTimeField(default=datetime.today())
    user_id = models.ForeignKey(UserMaster, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)   