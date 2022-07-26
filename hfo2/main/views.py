import datetime

from operator import is_not
import re
from unicodedata import category, name
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.views.generic import TemplateView, ListView
from main.models import CategoryModel, InstitutionModel, DonationModel
from main.forms import LoginForm, UserCreateForm, UserEditForm

# Create your views here.

    
    


class LandingPageView(View):
    def get(self, request):
        foundations = InstitutionModel.objects.filter(type="fundation")
        non_gov = InstitutionModel.objects.filter(type__contains="non_gov")
        local = InstitutionModel.objects.filter(type__contains="local")
        total_bags = sum([x.quantity for x in DonationModel.objects.all()])
        total_institutions = DonationModel.objects.all().distinct('institution').count()
        ctx = {
            'foundations' : foundations, 
            'non_gov': non_gov,
            'local': local,
            'total_bags':total_bags,
            'total_institutions': total_institutions,
        }
        return render(request, 'index.html', ctx)




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
        categories = CategoryModel.objects.all()
        ctx = {
             'categories': categories,
             }
         
        return render(request,'form.html',ctx)
    
    def post(self, request):
        categories_list = request.POST.getlist("categories")
        org_str = request.POST.get("organization")
        org_int = int(org_str)
        institution = InstitutionModel.objects.get(pk=org_int)
        
        data = DonationModel()
        data.quantity = request.POST.get("bags")
        data.address = request.POST.get("address")
        data.city = request.POST.get("city")
        data.zip_code = request.POST.get("postcode")
        data.phone_number = request.POST.get("phone")
        data.pick_up_date = request.POST.get("date")            
        data.pick_up_time = request.POST.get("time")
        data.pick_up_comment = request.POST.get("more_info")
        data.user = request.user
        data.institution = institution
        
        for category in categories_list:
            cat = CategoryModel.objects.get(pk=category)
            data.categories.add(cat)
                
        data.save()
        return redirect('/donationconfirm/')

       


class ConfirmView(TemplateView):
    template_name="form-confirmation.html"




class ShowMyDonationsView(ListView):
    model = DonationModel
    template_name = 'my_donations.html'
    pagination = 5
    
    def get_queryset(self, **kwargs):
       qs = super().get_queryset(**kwargs)
       return qs.filter(user=self.request.user)
       



#views for REST API:
def get_institutions_by_id(request):
    type_ids = request.GET.getlist('type_ids')
    if type_ids is not None:
        institutions = InstitutionModel.objects.filter(categories__pk__in=type_ids).distinct() 
    else:
        institutions = InstitutionModel.objects.all()
    return render(request, "api_ins.html", {'institutions':institutions,})            
            
 