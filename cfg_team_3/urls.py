from django.urls import path

from . import views

urlpatterns = [
    path('<str:name>', views.trackResponsesPerEvent, name='trackResponsesPerEvent'),
    path('<str:name>', views.trackResponsesDonor, name='trackResponsesDonor'),
    path('<str:name>', views.trackResponsesCustomer, name='trackResponsesCustomer'),
]
