from django.shortcuts import render,HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    # return HttpResponse("This is index page")
    context = {'name':'harry','course':'Django'}
    return render(request, 'home.html',context)

def about(request):
    # return HttpResponse("This is about page")
    return render(request, 'about.html')

def project(request):
    # return HttpResponse("This is project page")
    return render(request, 'project.html')

def contact(request):
    # return HttpResponse("This is contact page")
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
        phone = request.POST['phone']
        ins = Contact(name=name,email=email,phone=phone,desc=desc)
        ins.save()
        print("The data has been entered")
        # print(name,email,phone,desc)
    return render(request, 'contact.html')
