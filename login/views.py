from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
@login_required
def Profile_view(request):
    return render(request,'profile.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            login(request, user)
            return redirect('Profile_view')
    else:
        form = RegisterForm()
    return render(request, 'register1.html', {'form': form})

def login_view(request):
    # if request.method == 'POST':
    #     email = request.POST.get('email', '')
    #     password = request.POST.get('pass', '')
    #     user = authenticate(request, username=email, password=password)
        
    #     if user is not None:
    #         login(request, user)
    #         messages.success(request, "Logged in successfully!")
    #         return redirect('profile_view')
    #     else:
    #         messages.error(request, "Invalid credentials")
    
    # return render(request, 'index.html')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')
        
        try:
            user = User.objects.get(email=email)
            username = user.username  # Get the username associated with the email
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect('Profile_view')
            else:
                messages.error(request, "Invalid credentials")
        except User.DoesNotExist:
            messages.error(request, "Invalid credentials")
    
    return render(request, 'index.html')


def Logoutview(request):
    logout(request)
    return redirect('login') 