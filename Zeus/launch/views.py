###添加一个 我们前面提到的 index函数
#[root@localhost myapp]# vim views.py
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from . import case
import os
#coding=utf-8
#import time,simplejson,json,os,commands
 
# Create your views here.
def index(req):
        ##
        ##
        #return HttpResponse("aa")
        return render_to_response('add.html')
@csrf_exempt
def add(request):
    # mes = case.add(request)
    # return HttpResponse('新增成功')
        mes = case.add(request)
        #return HttpResponse('执行成功，请稍后去历史报告页面查看结果')
        cases = case.select(request)
        return render_to_response('result.html',{'cases':cases})

def add1(request):
        ##
        ##
        #return HttpResponse("aa")
        return render_to_response('add.html')

def result(request):
        cases = case.select(request)
        return render_to_response('result.html',{'cases':cases})

def details(request,testId):
        details = case.details(request,testId)
        return render_to_response('details.html',{'details':details})

def details2(request,testId):
    #detail = case.details(request,testId)
    details= case.details(request,testId)
    result = case.result(request,testId)
    device = case.device(request,testId)
    
    with open("/Users/jiangchun/Zeus/upload/test.txt", 'r') as f:
        log_txt=f.read()
    # /Users/jiangchun/myproject/upload/test.txt
    #return render_to_response('details2.html',{'detail_cold':detail_cold,'detail_hot':detail_hot})
    return render_to_response('details2.html',{'details':details,'result':result,'device':device,'log_txt':log_txt})