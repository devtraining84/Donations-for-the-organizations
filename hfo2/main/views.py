from unicodedata import category
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.views.generic import TemplateView, CreateView
from main.models import CategoryModel, InstitutionModel
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
    def get(self, request):
        categories = CategoryModel.objects.all()
        # institutions = InstitutionModel.objects.all()
        ctx = {
            'categories': categories,
            # 'institutions': institutions,
        }
        return render(request, 'form.html', ctx)
    
    def post(self, request):
        pass




def get_institutions_by_id(request):
    type_ids = request.GET.getlist('type_ids')
    if type_ids is not None:
        categories = CategoryModel.objects.filter(id__in=type_ids)
        institutions = InstitutionModel.objects.filter(categories__pk__in=type_ids) 
        info = type_ids
    else:
        categories = CategoryModel.objects.filter(id__in=type_ids)
        info = type_ids
    return render(request, "api_ins.html", {'info':info, 'categories': categories, 'institutions':institutions,})            
            
 