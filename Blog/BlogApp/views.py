from django.shortcuts import render,redirect
import yaml
import os
import os.path
import requests
from django.http import HttpResponse

# Create your views here.
from django.template import RequestContext
from django.views.decorators.csrf import ensure_csrf_cookie

path=""

def Home(request):
    return render(request, 'BlogApp/Home.html')

def Dashboard(request):
    return render(request, 'BlogApp/Dashboard.html')

def workflow(request):
    """
    This
    :param request:
    :return:
    """
    if request.method=="POST":
        name=request.POST['name']
        description = request.POST['description']
        step = request.POST.getlist('step[]')
        value={name : {'Description':description, 'Steps':step}}

        print(name,description,step)


    return HttpResponse('output')

            # The default_flow_style=False parameter is necessary to produce the format you want (flow style), otherwise for nested collections it produces block style:

@ensure_csrf_cookie
def workflowStepDetail(request):
    if request.method=="GET":
        blogData = request.GET.get('blogData')
        print("Blog Data : ", blogData)
    return HttpResponse('')

def workflowData(request):
    if request.method=="GET":
        blogData=request.GET.get('blogData')
        print('Sanyog : ',blogData)
    return HttpResponse('')

def get(request):
    context = RequestContext(request)
    context_dict = {}
    # Update the dictionary with csrf_token
    context_dict.update(csrf(request))
    return render_to_response("your_template.html", context_dict, context)