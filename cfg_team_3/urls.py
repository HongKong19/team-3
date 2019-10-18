from django.urls import path

from . import views

urlpatterns = [
    path('event/<str:name>', views.trackResponsesPerEvent, name='trackResponsesPerEvent'),
    path('donor-name/<str:name>', views.trackResponsesDonor, name='trackResponsesDonor'),
    path('customer-name/<str:name>', views.trackResponsesCustomer, name='trackResponsesCustomer'),
    path('lapse-donor', views.lapseDonor, name='lapseDonor'),
    path('potential-donor', views.potentialDonor, name='potentialDonor'),
    path('donation-history', views.showDonationHistory, name='showDonationHistory'),
    path('invited', views.showInvited, name='showInvited'),
    path('donors', views.showDonors, name='showDonors'),
    path('customers', views.showCustomers, name='showCustomers'),
]
