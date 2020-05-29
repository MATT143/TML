from django.shortcuts import render
from .serializers import createTicketSerializer,solutionCallbackFromEwsSerializer
from rest_framework.views import APIView
from .models import taskDetails
from rest_framework.response import Response
# Create your views here.




class createTicketView(APIView):
    def post(self,request):
        ser=createTicketSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=200)
        return Response(ser.errors,status=400)

class solutionCallbackFromEwsView(APIView):
    def post(self,request):
        ser=solutionCallbackFromEwsSerializer(data=request.data)
        if ser.is_valid():
            fetched_data=ser.data
            taskid=fetched_data.pop('task')
            query=taskDetails.objects.filter(taskId=taskid)
            query.update(**fetched_data)
            return Response(fetched_data,status=200)
        return Response(ser.errors,status=400)




