from django.db import models

# Create your models here.


# student info
class Student(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=20)


class Teacher(models.Model):
    tno = models.AutoField(primary_key=True)
    tname = models.CharField(max_length=20)


class learn(models.Model):
    sno = models.ForeignKey('Student', to_field='sno', on_delete=models.CASCADE)
    cname = models.CharField(max_length=20, default='')