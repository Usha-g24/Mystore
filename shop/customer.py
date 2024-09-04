from django.db import models

#Create your models here
class Customer(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.CharField(unique=True,max_length=9)
    password=models.CharField(max_length=9)
    mobile_number=models.CharField(max_length=10)


    #cheacking if email is  existing or not
    def isexit(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False
    
    #To check email id matching or not
    @staticmethod
    def getemail(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    
