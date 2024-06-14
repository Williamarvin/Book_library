from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def BookRepo(requests):
    return HttpResponseRedirect('https://crpf.gov.in/writereaddata/images/pdf/How_To_Stop_Worrying_And_Start_Living.pdf')