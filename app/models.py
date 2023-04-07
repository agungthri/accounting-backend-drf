from django.db import models

# Create your models here.

class Account(models.Model): 
    c1 = models.SmallIntegerField()
    c2 = models.SmallIntegerField()
    c3 = models.SmallIntegerField()
    c4 = models.SmallIntegerField()
    c5 = models.SmallIntegerField()
    c6 = models.SmallIntegerField()
    account = models.CharField(max_length=100)
    dp = models.CharField(max_length=2)

    class Meta:
        ordering = ['c1','c2','c3','c4','c5','c6',]
    
    def __str__(self) -> str:
        return f"{self.account}"

class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f"{self.date} - {self.type} - {self.desc}"
    


class Journal(models.Model):
    transaction = models.ForeignKey(Transaction, related_name="journal_transaction", on_delete=models.CASCADE)
    account = models.ForeignKey(Account, related_name="journal_account", on_delete=models.CASCADE)
    position = models.CharField(max_length=2)
    amount = models.IntegerField()