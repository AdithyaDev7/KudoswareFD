from django.shortcuts import render
from app1.forms import DetailForm
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.

#redirect paage to confirm submission
def confirmation(request):
    return render(request,'feed.html')

#to take the input from the form . if input present the redirect to next page , else remain in the same page
def register(request):
    if request.method=='POST':
        form=DetailForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h3>Registration Successful</h3>")
    else:
        form=DetailForm()
    return render(request,'register.html',{'form':form})

# this is the first welcome page of a company website
def welcome(request):
    return render(request,'welcome.html')
    
            


