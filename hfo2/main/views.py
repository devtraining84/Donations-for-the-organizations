from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.views.generic import TemplateView
from main.models import Category, Institution
from main.forms import DonationForm, LoginForm, UserCreateForm, UserEditForm

# Create your views here.

class LandingPageView(View):
    def get(self, request):
        # org1 = Institution.objects.filter(type__contains="fundacja")
        # org2 = Institution.objects.filter(type__contains="organizacj")
        # org3 = Institution.objects.filter(type__contains="lokalna")
        # ctx = {
        #     'org1': org1,
        #     'org2': org2,
        #     'org3': org3,
        # }
        return render(request, 'index.html', {})




class RegisterView(View):
    def get(self, request):
        form = UserCreateForm()
        return render(request, 'register.html', {'form': form})
    def post(self, request):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            del form.cleaned_data['password2']
            user = User.objects.create_user(**form.cleaned_data, email=form.cleaned_data['username'])
            return redirect('../login/#login-page')
        else:
            return render(request, 'register.html', {'form': form, 'error': 'error'})





class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    def post(self, request, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return redirect('../register/#register-page')
        else:
            text = 'Nie udało się zalogować'
            return render(request,
                        "login.html",
                        {'form': form, 'text': text})




class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')




class UserView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'user_view.html', {})





class SettingsUserView(View):
    def get(self, request):
        user = request.user
        form = UserEditForm(instance=user)
        return render(request, 'user_settings.html', {'form': form})
    def post(self, request):
        user = request.user
        passwd = User.objects.get(pk=request.user.id)
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            del form.cleaned_data['password2']
            if form.old_password == passwd.password:
                user.set_password(form.cleaned_data['password'])
                form.save()
        return redirect('/')





class AddDonationView(LoginRequiredMixin, View):
    def get(self, request):
        # category = Category.objects.all()
        # institution = Institution.objects.all()
        # ctx = {
        #     'category': category,
        #      'institution': institution,
        # }
        return render(request, 'form.html',{})
    
    # def post(self, request):
    #     form = DonationForm(request.POST)
    #     if form.is_valid():
    #         x = form.save(commit=False)
    #         x.user = request.user
    #         x.save()
    #         return redirect('/confirmation/')
    #     return redirect('/confirmation/')

    