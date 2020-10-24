from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class CustomUser(AbstractUser):
    user_type_data=((1,"Admin"),(2,"Department"),(3,"Peoples"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)


class AdminMD(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class Peoples(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    gender=models.CharField(max_length=255)
    address=models.TextField()
    mobile_number=models.IntegerField()
    aadhaar_number=models.IntegerField()
    district=models.CharField(max_length=255)
    legislative_assembly=models.CharField(max_length=255)
    panchayath=models.CharField(max_length=255)
    pincord=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now_add=True)
    objects=models.Manager()





class Department(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    

class Complaints(models.Model):
    id=models.AutoField(primary_key=True)
    description=models.CharField(max_length=255)
    people_id=models.ForeignKey(Peoples,on_delete=models.CASCADE)
    department_id=models.ForeignKey(Department,on_delete=models.CASCADE)


@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminMD.objects.create(admin=instance)
        if instance.user_type==2:
            Department.objects.create(admin=instance)
        if instance.user_type==3:
            Peoples.objects.create(admin=instance,mobile_number="",aadhaar_number="",district="",panchayath="",pincord="",legislative_assembly="",address="",gender="")


@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminmd.save()
    if instance.user_type==2:
        instance.department.save()
    if instance.user_type==3:
        instance.peoples.save()