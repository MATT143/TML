from django.urls import path,include
from .views import *

urlpatterns = [
    path('create/ticket/',createTicketView.as_view(),name='create-ticket'),
    path('solution/callback/',solutionCallbackFromEwsView.as_view(),name='solution-callback-esw'),
]