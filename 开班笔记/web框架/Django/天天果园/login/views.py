from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
# from ..register/models import *
# from ../register/forms import *

# Create your views here.

def login_views(request):
    if request.method == 'GET':
        return render(request, 'login_html')
    else:
        phone = request.POST['user']
        pwd = request.POST['pwd']

