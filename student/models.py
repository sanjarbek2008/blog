from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=250)



class Student(models.Model):
    teacher = models.ManyToManyField(Teacher)
    name = models.CharField(max_length=250)
