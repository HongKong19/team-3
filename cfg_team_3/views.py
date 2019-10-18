from django.shortcuts import render
from .models import Event, Donor, Customer, DonationHistory, Invitation

# Create your views here.

def trackResponsesPerEvent(request, name):
    eventResponseList = Invitation.objects.get(event_name=name).filter(attendance=1)
    donorNames = [e.donor_name for e in eventResponseList]
    customerNames = [e.customer_name for e in eventResponseList]
    output = donorNames + customerNames
    return HttpResponse(output)

def trackResponsesDonor(request, name):
    donorResponseList = Invitation.objects.get(donor_name=name).filter(attendance=1)
    output = ', '.join([e.event_name for e in donorResponseList])
    return HttpResponse(output)

def trackResponsesCustomer(request, name):
    customerResponseList = Invitation.objects.get(customer_name=name).filter(attendance=1)
    output = ', '.join([e.event_name for e in customerResponseList])
    return HttpResponse(output)
