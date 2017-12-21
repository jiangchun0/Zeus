from django.db import models

# Create your models here.

class Devices(models.Model):

	testId = models.BigAutoField(unique=True, primary_key=True)
	app_type = models.CharField(max_length=32,blank=True,null=True)
	test_type = models.CharField(max_length=32,blank=True,null=True)
	#app_url = models.CharField(max_length=100,blank=True,null=True)
	#app_url=models.FileField('文件',upload_to='./upload')
	app_version = models.CharField(max_length=32,blank=True, null=True)
	app_packageName = models.CharField(max_length=32,blank=True, null=True)
	device_name = models.CharField(max_length=32,blank=True, null=True)
	device_version = models.CharField(max_length=32,blank=True, null=True)
	time = models.CharField(max_length=32,blank=True, null=True)

class Result(models.Model):
	id = models.BigAutoField(unique=True, primary_key=True)
	testId = models.IntegerField()
	log_txt= models.CharField(max_length=100,blank=True)
	img_url= models.CharField(max_length=32,blank=True)
	# value_cold = models.FloatField(max_length=30,null=True)
	# value_hot =models.FloatField(max_length=30,null=True)

class Details(models.Model):
	id = models.AutoField(primary_key=True,null=False)
	testId = models.IntegerField()
	time = models.IntegerField()
	value_cold = models.CharField(max_length=30,null=True)
	value_hot = models.FloatField(max_length=30,null=False)

from django.http import HttpResponse
