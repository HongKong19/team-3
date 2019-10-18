from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    date = models.DateField()

class Donor(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)

class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

class DonationHistory(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=3)

class Invitation(models.Model):
    eventID = models.ForeignKey(Event, on_delete=models.CASCADE)
    donorID = models.ForeignKey(Donor, on_delete=models.CASCADE)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    attendance = models.BinaryField()
    registered = models.BinaryField()
    opened_link = models.BinaryField()
    def __str__(self):
        return self.eventID
