from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect


import datetime
from datetime import date

# Returns the current local date
today = date.today()
print(today)

end_date = today + datetime.timedelta(days=0)
print(end_date)

def messages():
    if end_date > today:
         messages.success("COMPLETE THE TASK")
         return HttpResponseRedirect()
        
