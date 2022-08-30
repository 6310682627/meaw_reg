from multiprocessing import Semaphore
from django.db import models

# Create your models here.


class Subject(models.Model):
    sub_id = models.CharField(max_length=64)
    sub_name = models.CharField(max_length=64)
    sem = models.CharField(max_length=64)
    year = models.CharField(max_length=64)
    max_seat = models.IntegerField()
    q_status = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{ self.id } : {self.sub_id} : {self.sub_name}"


class Student(models.Model):
    student_id = models.CharField(max_length=64)
    student_name = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{ self.id } : {self.student_id} : {self.student_name}"


class Apply(models.Model):
    
    sub_id = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="sub_apply")
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="stu_apply")

    def __str__(self):
        return f"{ self.id } : {self.sub_id} : {self.student_id}"
