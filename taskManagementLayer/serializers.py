from rest_framework import serializers
from .models import taskDetails

class createTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model=taskDetails
        fields=['custTaskId','userId','taskName','taskDescription','taskCategory','taskSubCategory','taskAttachment1',
                'taskAttachment2','taskStatus']

class solutionCallbackFromEwsSerializer(serializers.ModelSerializer):
    task=serializers.CharField(max_length=100)
    class Meta:
        model=taskDetails
        fields=['task','userId','solutionDescription','expertAssigned','solAttachment1','solAttachment2']