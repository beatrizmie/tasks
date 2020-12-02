from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from tasks.models import Task
from tasks.serializer import TaskSerializer
from django.forms.models import model_to_dict

def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

# GET all tasks
@csrf_exempt
def get_all_tasks(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, status=201, safe=False)

# GET task by id
@csrf_exempt
def get_task_by_id(request, task_id):
    if request.method == 'GET':
        task = Task.objects.get(pk=task_id)
        serializer = TaskSerializer(task)
        return JsonResponse(serializer.data, status=201, safe=False)

# POST task
@csrf_exempt
def create_task(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# UPDATE task title
@csrf_exempt
def update_task_title(request, task_id):
    if request.method == 'PUT':
        task = Task.objects.get(pk=task_id)
        data = JSONParser().parse(request)
        task.title = data['title']
        task.save()
        return JsonResponse(model_to_dict(task), status=201, safe=False)

# UPDATE task pub_date
@csrf_exempt
def update_task_pub_date(request, task_id):
    if request.method == 'PUT':
        task = Task.objects.get(pk=task_id)
        data = JSONParser().parse(request)
        task.pub_date = data['pub_date']
        task.save()
        return JsonResponse(model_to_dict(task), status=201, safe=False)

# UPDATE task description
@csrf_exempt
def update_task_description(request, task_id):
    if request.method == 'PUT':
        task = Task.objects.get(pk=task_id)
        data = JSONParser().parse(request)
        task.description = data['description']
        task.save()
        return JsonResponse(model_to_dict(task), status=201, safe=False)

# DELETE task
@csrf_exempt
def delete_task(request, task_id):
    if request.method == 'DELETE':
        task = Task.objects.get(pk=task_id)
        task.delete()
        return HttpResponse('Succesfully deleted task {0}'.format(task_id))

# DELETE all tasks
@csrf_exempt
def delete_all_tasks(request):
    if request.method == 'DELETE':
        task = Task.objects.all()
        task.delete()
        return HttpResponse('Succesfully deleted all tasks')