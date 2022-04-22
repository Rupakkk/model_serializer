# Create your views here.
from django.shortcuts import render
from django.views import View
from .models import Student
from .serializers import StudentModelSerializer
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from rest_framework.viewsets import ModelViewSet

from app import serializers

# Create your views here.
@method_decorator(csrf_exempt,name = 'dispatch')
class StudentView(View):

    
    def get(self,request,*args,**kwargs):
    
        json_data = request.body
        stream = io.BytesIO(json_data)
        print(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        print(python_data)  # If python data has any value then it gives it otherwise it gives None
        if id is not None:
            stu =  Student.objects.get(id=id)
            serializer = StudentModelSerializer(stu)
            json_data = JSONRenderer().render(serializer)
            return HttpResponse(json_data,content_type='application/json')
            return JsonResponse(serializer.data) 

        stu =  Student.objects.all()
        # serializer = StudentSerializer(stu, many=True)
        # return HttpResponse(serializer.data, content_type='application/json')
        return JsonResponse(serializer.data,safe=False)  # For non dictionary

            
    def post(self,request,*args,**kwargs):
        # if request.method == "POST":
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serialize = StudentModelSerializer(data = python_data)  # Important
        if serialize.is_valid():
            serialize.save()
            serializer = {'msg':'Data creation Successful'}
            return JsonResponse(serializer)
        else:
            data = JSONRenderer().render(serialize.errors)
            return HttpResponse(data,content_type = 'application/json')

    def put(self,request,*args,**kwargs):
        # if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serialize = StudentModelSerializer(stu,data = python_data)  # Important
        if serialize.is_valid():
            serialize.save()
            msg = {'msg':'Data creation Successful'}
            return JsonResponse(msg)
        return JsonResponse(serialize.errors)


    def delete(self,request,*args,**kwargs):
        # if request.method == "DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        msg = {'msg':'Data deletion Successful'}
        return JsonResponse(msg)
        

class TestViewSet(ModelViewSet):

    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()
