from datetime import datetime, timedelta
from django.contrib import messages
import random
from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.core.mail import send_mail
from .models import OTP

def SignupPage(request):
    if request.method == 'POST':
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        email = request.POST.get('email')
        password1 = request.POST.get('password')

        
        if User.objects.filter(email=email).exists():
            return HttpResponse("This email is already registered.")
        my_user= User.objects.create_user(username=email ,email=email , password=password1)
        my_user.first_name = fname
        my_user.last_name = lname
        my_user.save()

        otp = random.randint(100000, 999999)
        request.session["otp"] = otp
        request.session['email'] = email
        otp = OTP.objects.create(user=my_user, otp=otp)
        otp.save()

        send_mail(
            "Your OTP Code",
            f"Your OTP is {otp}. Please enter it to verify your identity.",
            "ch2953917@gmail.com",  # From
            [email],  # To (replace with user's email)
            fail_silently=False,
        )
        return redirect('verify')
    return render (request , 'signup.html')


# def OtpPage(request):
#     if request.method == 'POST':
#         entered_otp = request.POST.get('otp')
#         email = request.session.get('email')
        
#         if not email:
#             return HttpResponse("Session expired or invalid request.")

#         user = User.objects.get(email=email)
#         otp_instance = OTP.objects.filter(user=user, otp=entered_otp).latest('created_at')
#         otp_instance.is_valid = True
#         otp_instance.is_verified
#         otp_instance.save()
#         return redirect('login')

#     return render(request, 'otp.html')


def OtpPage(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        email = request.session.get('email')
        if not email:
            return HttpResponse("Session expired or invalid request.")
        try:
            user = User.objects.get(email=email)
            otp_instance = OTP.objects.filter(user=user, otp=entered_otp).latest('created_at')
            
            print(f"Entered OTP: {entered_otp}")
            print(f"Stored OTP: {otp_instance.otp}")
            print(f"OTP created at: {otp_instance.created_at}")

            otp_instance.is_verified = True
            otp_instance.save()
            return redirect('login')

        except User.DoesNotExist:
            return HttpResponse("User not found. Please sign up.")
        except OTP.DoesNotExist:
            return HttpResponse("Invalid OTP. Please try again.")

    return render(request, 'otp.html')



def LoginPage(request):
    if request.method == 'POST':
        email = request.POST.get('Email')
        password = request.POST.get('pass')
        user = authenticate(request, email = email ,username = email  ,  password = password)
        if user is not None:
            login(request,user)
            return redirect ('netflix/')
        else:
            return HttpResponse("username or password is incorrect")
    return render (request , 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')