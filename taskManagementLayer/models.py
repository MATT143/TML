from django.db import models
from django.utils.timezone import now
import uuid

class taskDetails(models.Model):
    taskId=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    custTaskId=models.CharField(max_length=100)
    userId=models.CharField(max_length=100)
    taskName=models.TextField()
    taskDescription=models.TextField()
    taskCategory=models.CharField(max_length=100)
    taskSubCategory=models.CharField(max_length=100)
    taskAttachment1=models.URLField(blank=True)
    taskAttachment2=models.URLField(blank=True)
    taskStatus=models.CharField(max_length=50)
    creationTime=models.DateTimeField(default=now())
    expertAssigned=models.CharField(max_length=200)
    solutionDescription=models.TextField()
    solAttachment1=models.URLField(blank=True)
    solAttachment2=models.URLField(blank=True)
    isPaid=models.BooleanField(default=False)

    def __str__(self):
        return self.taskId



