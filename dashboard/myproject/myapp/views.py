from django.shortcuts import render,redirect
from django.views import View
from .forms import RegisterForm,LogInForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

class home(View):

    def get(self,request):
        form = LogInForm()
        if request.user.is_authenticated is False:
            return render(request,'home.html',{'form':form})
        else:
            return redirect('blogs')

    def post(self,request):

        form = LogInForm(request.POST,data=request.POST)

        if form.is_valid():
            print('valid form')
            u_name = form.cleaned_data['username']
            u_pass = form.cleaned_data['password']
            print(u_name,u_pass)

            user = authenticate(username=u_name,password = u_pass)
            if user is not None:
                login(request,user)
                messages.success(request,f'Welcome {u_name} You have logged In Succesfully')
                return redirect('dashboard')
        messages.warning(request,'Something Went Wrong')
        return render(request,'home.html',{'form':form})


class register(View):

    def get(self,request):
        form = RegisterForm()
        return render(request,'register.html',{'form':form})

    def post(self,request):

        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        return render(request,'register.html',{'form':form})


class dashboard(View):

    def get(self,request):
        if request.user.is_authenticated:
            return render(request,'dashboard.html')
        else:
            return redirect('home')

    def post(self,request):
        return render(request,'dashboard.html')


class signout(View):

    def get(self,request):
        logout(request)
        messages.success(request,'Logged out succesfully')
        return redirect('home')
        
class blogs(View):
    
    def get(self,request):
            return render(request,'blogs.html')

            