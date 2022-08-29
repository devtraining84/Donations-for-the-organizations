import datetime
from operator import is_not
import re
from unicodedata import category, name
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.views.generic import TemplateView
from main.models import CategoryModel, InstitutionModel, DonationModel, TestModel2
from main.forms import LoginForm, UserCreateForm, UserEditForm

# Create your views here.

    
    


class LandingPageView(View):
    def get(self, request):
        foundations = InstitutionModel.objects.filter(type="fundation")
        non_gov = InstitutionModel.objects.filter(type__contains="non_gov")
        local = InstitutionModel.objects.filter(type__contains="local")
        ctx = {
            'foundations' : foundations, 
            'non_gov': non_gov,
            'local': local,
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
    # pass
    def get(self, request):
        categories = CategoryModel.objects.all()
        ctx = {
            'categories': categories,
            }
        return render(request, 'sub_form.html', ctx)
    
    def post(self, request):
        
       
        categories_list = request.POST.getlist("categories")
        categories = CategoryModel.objects.filter(name__in = categories_list)
        # pk or name, in depend on value in form
        
        

        data = TestModel2()
        data.quantity = request.POST.get("bags")
        data.address = request.POST.get("address")
        data.city = request.POST.get("city")
        data.zip_code = request.POST.get("postcode")
        data.phone_number = request.POST.get("phone")
        data.pick_up_date = request.POST.get("date")            
        data.pick_up_time = request.POST.get("time")
        #worktest
        data.pick_up_comment = request.POST.get("organization")
        
        #data.user = request.user.id
        
        
        data.save()
        return redirect('/donationconfirm/')

       




class ConfirmView(TemplateView):
    template_name="form-confirmation.html"



# class DonationModel(models.Model):
#     quantity = models.PositiveSmallIntegerField()
#     categories = models.ManyToManyField(CategoryModel)
#     institution = models.ForeignKey(InstitutionModel, on_delete=models.CASCADE)
#     address = models.CharField(max_length=40)
#     phone_number = models.PositiveIntegerField()
#     city = models.CharField(max_length=32)
#     zip_code = models.CharField(max_length=6)
#     pick_up_date = models.DateField()
#     pick_up_time = models.DateTimeField()
#     pick_up_comment = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default="Null")
    
#     def __str__(self):
#         return self.id



















def get_institutions_by_id(request):
    type_ids = request.GET.getlist('type_ids')
    if type_ids is not None:
        
        institutions = InstitutionModel.objects.filter(categories__pk__in=type_ids).distinct() 
       
    else:
        
        institutions = InstitutionModel.objects.all()
    return render(request, "api_ins.html", {'institutions':institutions,})            
            
 