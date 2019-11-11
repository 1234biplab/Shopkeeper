from django.db import models
from customer.models import Customer
from datetime import date

# Create your models here.

class PaymentType(models.Model):
    name=models.CharField(max_length=100,default='credit')

    def __str__(self):
        return self.name
class Register(models.Model):
    customer_name=models.ForeignKey(Customer,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=8,decimal_places=2)
    date=models.DateField(default=date.today())
    type=models.ForeignKey(PaymentType,on_delete=models.CASCADE)

    def __str__(self):
        return self.customer_name.name

