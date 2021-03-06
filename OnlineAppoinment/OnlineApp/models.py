from django.db import models


# Create your models here.
class AccDepartment(models.Model):
    Department = models.CharField(max_length=200, null=True)
    Depass = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.Department

class AccStudent(models.Model):
    Semail = models.EmailField(max_length=200, null=True)
    Spass = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.Semail

class AlumniBook(models.Model):
    Aname = models.CharField(max_length=200, null=True)
    Alast = models.CharField(max_length=200, null=True)
    Amail = models.EmailField(max_length=200, null=True)
    Asid = models.CharField(max_length=12, null=True)
    Acourse = models.CharField(max_length=200, null=True)
    Ayg = models.CharField(max_length=200, null=True)
    Adate = models.CharField(max_length=200, null=True)
    Adep = models.CharField(max_length=200, null=True)
    Apurp = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, default="Inbox")

    def __str__(self):
        return self.Aname

class StudentBook(models.Model):
    Sname = models.CharField(max_length=200, null=True)
    Slast = models.CharField(max_length=200, null=True)
    Smail = models.EmailField(max_length=200, null=True)
    Ssid = models.CharField(max_length=12, null=True)
    Scourse = models.CharField(max_length=200, null=True)
    Syear = models.CharField(max_length=200, null=True)
    Sdate = models.CharField(max_length=200, null=True)
    Sdep = models.CharField(max_length=200, null=True)
    Spurp = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, default="Inbox")
    
    
    

    def __str__(self):
        return self.Sname

class GuardianBook(models.Model):
    Ggname = models.CharField(max_length=200, null=True)
    Gname = models.CharField(max_length=200, null=True)
    Glast = models.CharField(max_length=200, null=True)
    Gmail = models.EmailField(max_length=200, null=True)
    Gsid = models.CharField(max_length=12, null=True)
    Gcourse = models.CharField(max_length=200, null=True)
    Gdate = models.CharField(max_length=200, null=True)
    Gdep = models.CharField(max_length=200, null=True)
    Gpurp = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, default="Inbox")
    
    
    def __str__(self):
        return self.Gname


