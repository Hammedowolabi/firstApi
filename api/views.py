from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
# from django.http import JsonResponse

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls ={
        'List':'/task-list/',
        'Detail View': '/task-list/<str:pk>/',
        'Create': '/tas-create/',
        'Update':'task-update/<str:pk>/',
        'Delete':'task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])

def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def taskDetail(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    # serializer represent your forms api create context
    serializer = TaskSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)




@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(data=request.data,instance=task)
     
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(data=request.data,instance=task)
    task.delete()

    return Response ('item successfully deleted')
