from django.db import models

class Party(models.Model):
    name=models.CharField(max_length=30)
    

    def __str__(self):
     return self.name

class Transactions(models.Model):
    party=models.ForeignKey(Party, on_delete=models.CASCADE)
    date=models.DateField()
    amount=models.SmallIntegerField(null=True,blank=True)
    description=models.CharField(max_length=30)
    trace=models.CharField(max_length=30)
    credit_debit=models.SmallIntegerField(null=True,blank=True)

    def __str__(self):
     return self.party



    