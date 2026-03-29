from django.db import models

class CustomerDB(models.Model):
    PhoneNo = models.IntegerField()
    Address = models.CharField(max_length=35)
    OrderNo = models.IntegerField(primary_key=True)
    Amount = models.IntegerField()
    Items = models.CharField(max_length=60)
    CustomerName = models.CharField(max_length=20)
    AdditionalNo = models.IntegerField()

    def __str__(self):
        return self.CustomerName