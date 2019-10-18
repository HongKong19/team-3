from django.shortcuts import render
from django.http import HttpResponse
from datetime import date


# Create your views here.

def index(request):
    return render(request, 'cfg_team_3/index.html')

def trackResponsesPerEvent(request, name):
    eventResponseList = []
    for i in Invitation:
        if (i[event_name]==name) and (i[attendance]==1):
            eventResponseList.append(i)
    donorNames = [e[donor_name] for e in eventResponseList]
    customerNames = [e[customer_name] for e in eventResponseList]
    output = donorNames + customerNames
    return HttpResponse(output)

def trackResponsesDonor(request, name):
    donorResponseList = []
    for i in Invitation:
        if (i[donor_name]==name) and (i[attendance]==1):
            donorResponseList.append(i)
    output = [e[event_name] for e in donorResponseList]
    return HttpResponse(output)

def trackResponsesCustomer(request, name):
    customerResponseList = []
    for i in Invitation:
        if (i[customer_name]==name) and (i[attendance]==1):
            customerResponseList.append(i)
    output = [e[event_name] for e in customerResponseList]
    return HttpResponse(output)

def lapseDonor(request):

    donorNames = []
    for dh in DonationHistory:
        if ((date.today()-dh[date]).days>30):
            donorNames.append(dh[donor_name])
    donorEmails = []
    for name in donorNames:
        for d in donor:
            if (d[donor_name]==name):
                donorEmails.append(d[email])
    return HttpResponse(donorEmails)

def potentialDonor(request):
    donorNames = []
    for dh in DonationHistory:
        if (dh[amount]>=300):
            donorNames.append(dh[donor_name])
    donorEmails = []
    for name in donorNames:
        for d in donor:
            if (d[donor_name] == name):
                donorEmails.append(d[email])
    return HttpResponse(donorEmails)


def index(request):
    return render(request, 'cfg_team_3/index.html')


