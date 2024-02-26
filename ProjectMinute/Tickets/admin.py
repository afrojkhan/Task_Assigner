from django.contrib import admin

# Register your models here.
from .models import StateMaster,UserMaster,TaskMaster

@admin.register(StateMaster)
class StateModel(admin.ModelAdmin):
    list_display = ['id','state_name','state_code','created_date','updated_date','is_active']


@admin.register(UserMaster)
class UserModel(admin.ModelAdmin):

    list_display = ['id','name','email','password','phone','city','gender','joining_date','state','created_date','updated_date','is_active']

@admin.register(TaskMaster)
class TaskModel(admin.ModelAdmin):

    list_display = ['id','task_id','title','description','assign_date','state','created_date','updated_date','user_id','is_active']