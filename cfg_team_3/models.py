from django.db import models

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=50, primary_key=True)
    description = models.CharField(max_length=50)
    date = models.DateField()
    category = models.CharField(max_length=30)

class Donor(models.Model):
    donor_name = models.CharField(max_length=50, primary_key=True)
    email = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)

class Customer(models.Model):
    customer_name = models.CharField(max_length=50, primary_key=True)
    email = models.CharField(max_length=50)

class Attendee(models.Model):
    donor_name = models.ForeignKey(Donor, on_delete=models.CASCADE)
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)

class DonationHistory(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=3)

class Invitation(models.Model):
    event_name = models.ForeignKey(Event, on_delete=models.CASCADE)
    donor_name = models.ForeignKey(Donor, on_delete=models.CASCADE)
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    attendance = models.BinaryField()
    registered = models.BinaryField()
    opened_link = models.BinaryField()
    def __str__(self):
        return self.eventID
