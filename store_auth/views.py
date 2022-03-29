from django.shortcuts import render, redirect
from .models import UserRegister
from django.views import View
from django.contrib.auth.hashers import make_password
# Create your views here.
class UserRegisterView(View):
    def get(self, request):
    
        return render(request, 'store_auth/signup.html')
    def post(self, request):
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        phone_number = data.get('phone_number')
        email = data.get('email')
        password = data.get('password')
        value = {
            'first_name' : first_name,
            'last_name' : last_name,
            'phone_number' : phone_number,
            'email' : email,
        }
        error_message = None

        userreg = UserRegister(first_name = first_name,
                                last_name= last_name,
                                phone_number= phone_number,
                                email=email,
                                password=password)
        # error_message = self.validateUserRegister(userreg)

        if not error_message:
            print(first_name, last_name, phone_number, email, password)
            userreg.password = make_password(userreg.password)
            userreg.save()
            return redirect('index')
        else:
            data = {
                'error' : error_message,
                'values' : value
            }
            return render(request, 'store_auth/signup.html', data)