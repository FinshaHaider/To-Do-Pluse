from django.db import models

# Create your models here.
class Tasks(models.Model):
    task=models.CharField(max_length=20)
    priority=models.IntegerField()
    deadline=models.DateField()

    def __str__(self):
        return self.task
    
class Todo(models.Model):
    task=models.CharField(max_length=20)
    completed=models.BooleanField(default=False)
    
      
    def __str__(self):
        return self.task
    
class Users(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.username



class Notes(models.Model):
    title=models.CharField(max_length=20)
    content=models.TextField()

    def __str__(self):
        return self.title


    
# class Task_details(models.Model):
#     task_id=models.ForeignKey(Tasks, on_delete=models.CASCADE)
#     description=models.TextField()
#     due_date=models.DateField()
#     completed=models.BooleanField(default=False)
#     created_at=models.DateTimeField(auto_now_add=True)
