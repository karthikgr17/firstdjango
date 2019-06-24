from django.shortcuts import render
from .forms import Bookforms
from .models import Book 
# Create your views here.
def form_view(request):
    if request.method =='POST':
        form=BookForms(request.POST)
        if 
    form=customforms()
    context={
        'head':'Custom form created using python',
        'forms':form
    }
    return render(request,'forms.html',context)