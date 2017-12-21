from django.http import HttpResponse
from launch.models import Devices
from launch.models import Result
from launch.models import Details
import time
import os
def add(request):
    datetime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # obj = request.FILES.get("app_url",None)
    # f = open(os.path.join('upload',obj.name),'wb')
    # for line in obj.chunks():
    #     f.write(line)
    # f.close()
    # if request.method == 'POST':
    #     my_form = FileUploadForm(request.POST, request.FILES)
    if request.method=="POST":  
        files = request.FILES.getlist('app_url') 
        # handle_upload_file(files,str(request.FILES['app_url'])) 
        handle_upload_file(request.FILES['app_url'],str(request.FILES['app_url']))          
    
    cases = Devices(
        app_type=request.POST['app_type'],
        test_type=request.POST['test_type'],
        app_version=request.POST['app_version'],
        device_name=request.POST['device_name'],
        device_version=request.POST['device_version'],
        time =datetime,
        app_packageName=request.POST['app_packageName'],
        )
    cases.save()
    result_id = cases.testId
    return result_id

def select(request):
     cases = Devices.objects.all().order_by("-testId")
     return cases

def result(request,testId):
     result = Result.objects.filter(testId=testId)
     return result

def device(request,testId):
     device = Devices.objects.filter(testId=testId)
     return device

def details(request,testId):
        #details = Details.objects.filter(testId=testId).order_by("time")
        # for i in detail_cold:
        details = Details.objects.filter(testId=testId).order_by("time")
        return details

def handle_upload_file(file,filename):  
    path='./upload/'     #上传文件的保存路径，可以自己指定任意的路径 
    if not os.path.exists(path):  
        os.makedirs(path) 
    with open(path+filename,'wb+')as destination:  
        for chunk in file.chunks():  
            destination.write(chunk)
    # for f in file:        
    #     dest= open(path+filename + f.name,'wb+')  
    #     for chunk in f.chunks():
    #         dest.write(chunk)  
    #     dest.close() 
 
        