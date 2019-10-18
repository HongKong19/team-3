from django.shortcuts import render
from cfg_team_3.models import Event, Donor, Customer, DonationHistory, Invitation
from django.http import HttpResponse
from datetime import date
import json


# Create your views here.

def trackResponsesPerEvent(request, name):
    customer1 = dict()
    customer1 = { 'customer_name' : 'John Harrow', 'email' : 'john22@gmail.com', 'net_worth' : 200000}
    customer2 = { 'customer_name' : 'Ash Green', 'email' : 'ash_green@gmail.com', 'net_worth' : 1000000}
    customer = [customer1, customer2]
    donor1 = { 'donor_name' : 'Lui Chun Kit',
        'email' : 'lui@gmail.com',
        'country' : 'Hong Kong',
        'company' : 'Steep Consulting Limited',
        'occupation' : 'Businessman'
    }

    donor2 = { 'donor_name' : 'Jeffrey Archer',
        'email' : 'ja@gmail.com',
        'country' : 'England',
        'company' : 'Bloomburry Lmt',
        'occupation' : 'Businessman'
    }

    donor = [donor1, donor2]

    invitation1 = { 'event_name' : 'Lama Music Festival',
        'donor_name' : 'Lui Chun Kit',
        'customer_name' : '',
        'attendance' : True,
        'registered' : True,
        'opened_link' : True
    }

    invitation2 = { 'event_name' : 'Zodiax Music Festival',
        'donor_name' : '',
        'customer_name' : 'Harry Kane',
        'attendance' : True,
        'registered' : True,
        'opened_link' : True
    }

    invitation = [invitation1, invitation2]

    donation_history1 = { 'donor_name' : 'Lui Chun Kit',
        'date' : date(2015, 8, 12),
        'amount' : 5000
    }

    donation_history2 = { 'donor_name' : 'Jeffrey Archer',
        'date' : date(2017, 9, 21),
        'amount' : 5000
    }

    donation_history = [donation_history1, donation_history2]

    eventResponseList = []
    for i in invitation:
        if (i['event_name']==name) and (i['attendance']==1):
            eventResponseList.append(i)
    donorNames = [e['donor_name'] for e in eventResponseList]
    customerNames = [e['customer_name'] for e in eventResponseList]
    output = donorNames + customerNames
    return HttpResponse(output)

def trackResponsesDonor(request, name):
    customer1 = dict()
    customer1 = { 'customer_name' : 'John Harrow', 'email' : 'john22@gmail.com', 'net_worth' : 200000}
    customer2 = { 'customer_name' : 'Ash Green', 'email' : 'ash_green@gmail.com', 'net_worth' : 1000000}
    customer = [customer1, customer2]
    donor1 = { 'donor_name' : 'Lui Chun Kit',
        'email' : 'lui@gmail.com',
        'country' : 'Hong Kong',
        'company' : 'Steep Consulting Limited',
        'occupation' : 'Businessman'
    }

    donor2 = { 'donor_name' : 'Jeffrey Archer',
        'email' : 'ja@gmail.com',
        'country' : 'England',
        'company' : 'Bloomburry Lmt',
        'occupation' : 'Businessman'
    }

    donor = [donor1, donor2]

    invitation1 = { 'event_name' : 'Lama Music Festival',
        'donor_name' : 'Lui Chun Kit',
        'customer_name' : '',
        'attendance' : True,
        'registered' : True,
        'opened_link' : True
    }

    invitation2 = { 'event_name' : 'Zodiax Music Festival',
        'donor_name' : '',
        'customer_name' : 'Harry Kane',
        'attendance' : True,
        'registered' : True,
        'opened_link' : True
    }

    invitation = [invitation1, invitation2]

    donation_history1 = { 'donor_name' : 'Lui Chun Kit',
        'date' : date(2015, 8, 12),
        'amount' : 5000
    }

    donation_history2 = { 'donor_name' : 'Jeffrey Archer',
        'date' : date(2017, 9, 21),
        'amount' : 5000
    }

    donation_history = [donation_history1, donation_history2]

    donorResponseList = []
    for i in invitation:
        if (i['donor_name']==name) and (i['attendance']==1):
            donorResponseList.append(i)
    output = [e['event_name'] for e in donorResponseList]
    return HttpResponse(output)

def trackResponsesCustomer(request, name):
    customer1 = dict()
    customer1 = { 'customer_name' : 'John Harrow', 'email' : 'john22@gmail.com', 'net_worth' : 200000}
    customer2 = { 'customer_name' : 'Ash Green', 'email' : 'ash_green@gmail.com', 'net_worth' : 1000000}
    customer = [customer1, customer2]
    donor1 = { 'donor_name' : 'Lui Chun Kit',
        'email' : 'lui@gmail.com',
        'country' : 'Hong Kong',
        'company' : 'Steep Consulting Limited',
        'occupation' : 'Businessman'
    }

    donor2 = { 'donor_name' : 'Jeffrey Archer',
        'email' : 'ja@gmail.com',
        'country' : 'England',
        'company' : 'Bloomburry Lmt',
        'occupation' : 'Businessman'
    }

    donor = [donor1, donor2]

    invitation1 = { 'event_name' : 'Lama Music Festival',
        'donor_name' : 'Lui Chun Kit',
        'customer_name' : '',
        'attendance' : True,
        'registered' : True,
        'opened_link' : True
    }

    invitation2 = { 'event_name' : 'Zodiax Music Festival',
        'donor_name' : '',
        'customer_name' : 'Harry Kane',
        'attendance' : True,
        'registered' : True,
        'opened_link' : True
    }

    invitation = [invitation1, invitation2]

    donation_history1 = { 'donor_name' : 'Lui Chun Kit',
        'date' : date(2015, 8, 12),
        'amount' : 5000
    }

    donation_history2 = { 'donor_name' : 'Jeffrey Archer',
        'date' : date(2017, 9, 21),
        'amount' : 5000
    }

    donation_history = [donation_history1, donation_history2]
    customerResponseList = []
    for i in invitation:
        if (i['customer_name']==name) and (i['attendance']==1):
            customerResponseList.append(i)
    output = [e['event_name'] for e in customerResponseList]
    return HttpResponse(output)

def lapseDonor(request):

    customer1 = dict()
    customer1 = { 'customer_name' : 'John Harrow', 'email' : 'john22@gmail.com', 'net_worth' : 200000}
    customer2 = { 'customer_name' : 'Ash Green', 'email' : 'ash_green@gmail.com', 'net_worth' : 1000000}
    customer = [customer1, customer2]
    donor1 = { 'donor_name' : 'Lui Chun Kit',
        'email' : 'lui@gmail.com',
        'country' : 'Hong Kong',
        'company' : 'Steep Consulting Limited',
        'occupation' : 'Businessman'
    }

    donor2 = { 'donor_name' : 'Jeffrey Archer',
        'email' : 'ja@gmail.com',
        'country' : 'England',
        'company' : 'Bloomburry Lmt',
        'occupation' : 'Businessman'
    }

    donor = [donor1, donor2]

    invitation1 = { 'event_name' : 'Lama Music Festival',
        'donor_name' : 'Lui Chun Kit',
        'customer_name' : '',
        'attendance' : True,
        'registered' : True,
        'opened_link' : True
    }

    invitation2 = { 'event_name' : 'Zodiax Music Festival',
        'donor_name' : '',
        'customer_name' : 'Harry Kane',
        'attendance' : True,
        'registered' : True,
        'opened_link' : True
    }

    invitation = [invitation1, invitation2]

    donation_history1 = { 'donor_name' : 'Lui Chun Kit',
        'date' : date(2015, 8, 12),
        'amount' : 5000
    }

    donation_history2 = { 'donor_name' : 'Jeffrey Archer',
        'date' : date(2017, 9, 21),
        'amount' : 5000
    }

    donationhistory = [donation_history1, donation_history2]
    donorNames = []
    for dh in donationhistory:
        if ((date.today()-dh['date']).days>30):
            donorNames.append(dh['donor_name'])
    donorEmails = []
    for name in donorNames:
        for d in donor:
            if (d['donor_name']==name):
                donorEmails.append(d['email'])
    json_stuff = json.dumps({"emails" : donorEmails})
    return HttpResponse(json_stuff, content_type ="application/json")
    return HttpResponse(donorEmails)

def potentialDonor(request):
    customer1 = dict()
    customer1 = { 'customer_name' : 'John Harrow', 'email' : 'john22@gmail.com', 'net_worth' : 200000}
    customer2 = { 'customer_name' : 'Ash Green', 'email' : 'ash_green@gmail.com', 'net_worth' : 1000000}
    customer = [customer1, customer2]
    donor1 = { 'donor_name' : 'Lui Chun Kit',
        'email' : 'lui@gmail.com',
        'country' : 'Hong Kong',
        'company' : 'Steep Consulting Limited',
        'occupation' : 'Businessman'
    }

    donor2 = { 'donor_name' : 'Jeffrey Archer',
        'email' : 'ja@gmail.com',
        'country' : 'England',
        'company' : 'Bloomburry Lmt',
        'occupation' : 'Businessman'
    }

    donor = [donor1, donor2]

    invitation1 = { 'event_name' : 'Lama Music Festival',
        'donor_name' : 'Lui Chun Kit',
        'customer_name' : '',
        'attendance' : True,
        'registered' : True,
        'opened_link' : True
    }

    invitation2 = { 'event_name' : 'Zodiax Music Festival',
        'donor_name' : '',
        'customer_name' : 'Harry Kane',
        'attendance' : True,
        'registered' : True,
        'opened_link' : True
    }

    invitation = [invitation1, invitation2]

    donation_history1 = { 'donor_name' : 'Lui Chun Kit',
        'date' : date(2015, 8, 12),
        'amount' : 5000
    }

    donation_history2 = { 'donor_name' : 'Jeffrey Archer',
        'date' : date(2017, 9, 21),
        'amount' : 5000
    }
    donationhistory = [donation_history1, donation_history2]
    donorNames = []
    for dh in donationhistory:
        if (dh['amount']>=300):
            donorNames.append(dh['donor_name'])
    donorEmails = []
    for name in donorNames:
        for d in donor:
            if (d['donor_name'] == name):
                donorEmails.append(d['email'])
    json_stuff = json.dumps({"emails" : donorEmails})
    return HttpResponse(json_stuff, content_type ="application/json")

def showDonationHistory(request):
    donation_history1 = { 'donor_name' : 'Lui Chun Kit',
        'date' : date(2015, 8, 12),
        'amount' : 5000
    }

    donation_history2 = { 'donor_name' : 'Jeffrey Archer',
        'date' : date(2017, 9, 21),
        'amount' : 5000
    }
    donationhistory = [donation_history1, donation_history2]
    json_stuff = json.dumps({"donationHistory" : donationhistory})
    return HttpResponse(json_stuff, content_type ="application/json")

def showInvited(request):
    invitation1 = { 'event_name' : 'Lama Music Festival',
        'donor_name' : 'Lui Chun Kit',
        'customer_name' : '',
        'attendance' : True,
        'registered' : True,
        'opened_link' : True
    }

    invitation2 = { 'event_name' : 'Zodiax Music Festival',
        'donor_name' : '',
        'customer_name' : 'Harry Kane',
        'attendance' : True,
        'registered' : True,
        'opened_link' : True
    }

    invitation = [invitation1, invitation2]
    json_stuff = json.dumps({"invited" : invitation})
    return HttpResponse(json_stuff, content_type ="application/json")

def showDonors(request):
    donor1 = { 'donor_name' : 'Lui Chun Kit',
        'email' : 'lui@gmail.com',
        'country' : 'Hong Kong',
        'company' : 'Steep Consulting Limited',
        'occupation' : 'Businessman'
    }

    donor2 = { 'donor_name' : 'Jeffrey Archer',
        'email' : 'ja@gmail.com',
        'country' : 'England',
        'company' : 'Bloomburry Lmt',
        'occupation' : 'Businessman'
    }

    donor = [donor1, donor2]
    json_stuff = json.dumps({"donors" : donor})
    return HttpResponse(json_stuff, content_type ="application/json")

def showCustomers(request):
    customer1 = { 'customer_name' : 'John Harrow', 'email' : 'john22@gmail.com', 'net_worth' : 200000}
    customer2 = { 'customer_name' : 'Ash Green', 'email' : 'ash_green@gmail.com', 'net_worth' : 1000000}
    customer = [customer1, customer2]
    json_stuff = json.dumps({"customers" : customer})
    return HttpResponse(json_stuff, content_type ="application/json")
