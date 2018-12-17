from django.urls import path

from Dashboard.views import *

app_name = 'Dashboard'  # APP_NAME

urlpatterns = [
    path('', dashboard, name='home'),

]
