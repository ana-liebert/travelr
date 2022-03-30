from django.urls import path
from . import views



urlpatterns = [
    path('', views.StarterView.as_view(), name="starter"),
    path('about/', views.About.as_view(), name="about"),
    path('accounts/signup', views.Signup.as_view(), name = "signup"),
    path('profile/<int:pk>', views.ProfilePage.as_view(), name = "profile"),
    path('profile_update/<int:pk>', views.ProfileUpdate.as_view(), name ="profile_update"),
    path('city/add', views.CityCreate.as_view(), name = "city_create"),
    path('city/<int:pk>', views.CityDetail.as_view(), name="city_detail"),
    path('city/guides/add', views.GuideCreate.as_view(), name="guide_create"),
    path('guides/<int:pk>', views.GuideDetail.as_view(), name="guide_detail"),
    path('guide_update/<int:pk>', views.GuideUpdate.as_view(), name ="guide_update"),
    path('guide_delete/<int:pk>', views.GuideDelete.as_view(), name ="guide_delete"),
    path('city_delete/<int:pk>', views.CityDelete.as_view(), name ="city_delete"),
    path('city_update/<int:pk>', views.CityUpdate.as_view(), name ="city_update"),
]