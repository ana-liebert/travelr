from django.urls import path
from . import views
from .views import Signup



urlpatterns = [
    path('', views.StarterView.as_view(), name="starter"),
    path('about/', views.About.as_view(), name="about"),
    path('accounts/signup', views.Signup.as_view(), name = "signup"),
    path('profile/<int:pk>/', views.ProfilePage.as_view(), name = "profile"),
    path('<int:pk>/profile_update/', views.ProfileUpdate.as_view(), name ="profile_update"),
    path('city/add', views.CityCreate.as_view(), name = "city_create")
]