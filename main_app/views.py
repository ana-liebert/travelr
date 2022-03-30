from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Profile, City, Guide, User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView, View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import UserProfileForm, GuideCreateForm, UpdateProfileForm, UpdateGuideForm, CityCreateForm
from django.urls import reverse

# Create your views here.


class StarterView(TemplateView):
    template_name = 'starter.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city=self.request.GET.get("city")
        if city != None: 
            context["cities"] = City.objects.filter(name__icontains=city)
        else: 
            context["cities"] = City.objects.all()
        
        return context
    


class About(TemplateView):
    template_name = "about.html"

class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        profile_form = UserProfileForm()
        context = {"form": form, "profile_form": profile_form}
        return render(request, "registration/signup.html", context)
    # on form ssubmit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect("starter")
        else:
            context = {"form": form, "profile_form": profile_form}
            return render(request, "registration/signup.html", context)

@method_decorator(login_required, name='dispatch')
class ProfilePage(DetailView):
    model = Profile
    template_name = "profile.html"
    def get_context_data(self, **kwargs):
        context = super(ProfilePage, self).get_context_data(**kwargs)
        context['guide'] = Guide.objects.filter(user=self.request.user)
        return context

@method_decorator(login_required, name='dispatch')
class CityCreate(CreateView):
    model = City
    form_class = CityCreateForm
    template_name = "city_create.html"
    # fields = ['name', 'image', 'country', 'grid_img']
    
    #TODO: Change this to bring you to the city detail view when its done
    def get_success_url(self):
        return reverse('city_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    # fields = ['first_name', 'last_name', 'city', 'profile_pic', ]
    template_name = "profile_update.html"
    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})


class CityDetail(DetailView):
    model = City
    template_name = "city_show.html"
    
    def get_context_data(self, **kwargs):
        context = super(CityDetail, self).get_context_data(**kwargs)
        context['guide'] = Guide.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class GuideCreate(View):
    
    def get(self, request):
        form = GuideCreateForm()
        form_class = GuideCreateForm
        context = {"form": form}
        print("this is what printing looks like")
        return render(request, "guide_create.html", context)

    def post(self, request):
        print(request.user.id)
        form = GuideCreateForm(request.POST)
        if form.is_valid():
            print("valid")
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect("starter")
        else:
            context = {"form": form}
            return render(request, "guide_create.html", context)


class GuideDetail(DetailView):
    model = Guide
    template_name = "guide_detail.html"


@method_decorator(login_required, name='dispatch')
class GuideUpdate(UpdateView):
    model = Guide
    form_class = UpdateGuideForm

    template_name = "guide_update.html"
    def get_success_url(self):
        return reverse('guide_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class GuideDelete(DeleteView):
    model = Guide
    template_name = "delete_confirmation.html"
    success_url = "/"

@method_decorator(login_required, name='dispatch')
class CityDelete(DeleteView):
    model = City
    template_name = "delete_confirmation.html"
    success_url = "/"

@method_decorator(login_required, name='dispatch')
class CityUpdate(UpdateView):
    model = City
    fields = ['name', 'image', 'country', 'grid_img', ]

    template_name = "city_update.html"
    def get_success_url(self):
        return reverse('city_detail', kwargs={'pk': self.object.pk})

