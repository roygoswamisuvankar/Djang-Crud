from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #if request.method == "POST":
        #my_data = request.POST.get('text1')
        #print(my_data)
    return render(request,'base.html', {'name':'Suvankar'})
#took data from html form, def function, set path in urls.py
"""def add(request):
    if request.method == "POST":
        val = request.POST.get('text1')
        val1 = request.POST.get('text2')
        if(val == ''):
            text = "*Field is required"
            return render(request,'base.html',{'text':text, 'name':'suvankar'})
        else:
            sum = int(val)+int(val1)
            return render(request,'base.html',{'result':sum})"""

