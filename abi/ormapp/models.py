from django.db import models
from django.contrib import admin
class Bank(models.Model):
	Name=models.CharField(max_length=30)
	Accno=models.IntegerField(primary_key=True)
	Adharno=models.IntegerField()
	DoB=models.DateField()
	Branch=models.CharField(max_length=20)
class BankAdmin(admin.ModelAdmin):
	list_display=("Name","Accno","Adharno","DoB","Branch")