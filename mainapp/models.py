from django.db import models
from datetime import datetime


class Branche(models.Model):
    branch_name= models.CharField(max_length=100)
    street=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    def __str__(self):
        return self.branch_name


class Trainer(models.Model):
    trainer_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    specialized = models.CharField(max_length=50)
    def __str__(self):
        return self.trainer_name


class Event(models.Model):
    branch=models.ForeignKey(Branche, on_delete=models.DO_NOTHING)
    trainer_name= models.ForeignKey(Trainer, on_delete=models.DO_NOTHING)
    event_name=models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    date = models.DateTimeField(blank=True, null=True)
    class_duration=models.CharField(max_length=50)
    seats=models.IntegerField()
    is_published=models.BooleanField(default=True)
    def __str__(self):
            return self.event_name

class Enrollment (models.Model):
    event=models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    branch=models.ForeignKey(Branche, on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    def __str__(self):
            return self.name




