from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import student
from django.db import connection

def index(request):
    #if request.method == "POST":
        #my_data = request.POST.get('text1')
        #print(my_data)
    return render(request,'base.html', {'name':'Suvankar'})
#took data from html form, def function, set path in urls.py
def add(request):
    if request.method == "POST":
        val = request.POST.get('text1')
        val1 = request.POST.get('text2')
        if(val == ''):
            text = "*Field is required"
            return render(request,'base.html',{'text':text, 'name':'suvankar'})
        else:
            sum = int(val)+int(val1)
            return render(request,'base.html',{'result':sum})
            
            #action name as function name
            '''def action_name(request):
                ...
                :return render(request,'new_html_file.html')'''

#function of new html file
def new(request):
    return render(request,'new.html')
#function of fibonaci series under new html file
def fibo(request):
    if request.method == "POST":
        val = request.POST.get('text1')
        n = int(val)
        a = 0
        b = 1
        i=0
        while(i<=n):
            #print(a)
            context = {
                'result' : a
            }
            next = a + b
            a = b
            b = next
            i=i+1
    return render(request, 'new.html', context)

#view all data from mysql create 'show' function
def show(request):
    data = student.objects.all()
    return render(request,'show.html',{'data' : data})

#insertdata function to save data into it
def insertdata(request):
    #insert data into database
    if(request.method == "POST"):
        id = request.POST.get('id')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        save_data = student(id,name,phone,email)
        save_data.save()

    # after submiting data it will refesh the page and reload all data from database
    data = student.objects.all()
    return render(request, 'show.html', {'data': data })

#delete function
def delete(request, id):
    st = student.objects.get(id=id)
    st.delete()
    return redirect("show")

#edit function
def edit(request, id):
    ed = student.objects.get(id=id)
    return render(request, 'edit.html',{'data' : ed } )

#update data
def update(request):

    if (request.method == "POST"):
        id = request.POST.get('id')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        update_data = student(id, name, phone, email)
        update_data.save()
    return redirect("show")

#searching data


