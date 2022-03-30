from django import forms
from .models import Guide, Profile, City

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'city', 'profile_pic')

    widgets = {
        'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        'city': forms.TextInput(attrs={'class': 'form-control'}),
        'profile_pic': forms.TextInput(attrs={'class': 'form-control'}),
    }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'city', 'profile_pic')

class GuideCreateForm(forms.ModelForm):
    class Meta:
        model = Guide
        fields = ('title', 'city', 'country', 'neighborhood', 'description', 'category', 'image', 'image2', 'image3', 'image4', 'image5' )

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'city': forms.Select(attrs={'class': 'form-control'}),
        'country': forms.TextInput(attrs={'class': 'form-control'}),
        'neighborhood': forms.TextInput(attrs={'class': 'form-control'}),
        'description': forms.Textarea(attrs={'class': 'form-control'}),
        'category': forms.TextInput(attrs={'class': 'form-control'}),
        'image': forms.TextInput(attrs={'class': 'form-control'}),
        'image2': forms.TextInput(attrs={'class': 'form-control'}),
        'image3': forms.TextInput(attrs={'class': 'form-control'}),
        'image4': forms.TextInput(attrs={'class': 'form-control'}),
        'image5': forms.TextInput(attrs={'class': 'form-control'}),
    }
    

class UpdateGuideForm(forms.ModelForm):
    class Meta:
        model = Guide
        fields = ('title', 'country', 'neighborhood', 'description', 'category', 'image',
        'image2',
        'image3',
        'image4',
        'image5')

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'country': forms.TextInput(attrs={'class': 'form-control'}),
        'neighborhood': forms.TextInput(attrs={'class': 'form-control'}),
        'description': forms.TextInput(attrs={'class': 'form-control'}),
        'category': forms.TextInput(attrs={'class': 'form-control'}),
        'image': forms.TextInput(attrs={'class': 'form-control'}),
        'image2': forms.TextInput(attrs={'class': 'form-control'}),
        'image3': forms.TextInput(attrs={'class': 'form-control'}),
        'image4': forms.TextInput(attrs={'class': 'form-control'}),
        'image5': forms.TextInput(attrs={'class': 'form-control'}),
    }

class CityCreateForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('name', 'image', 'country', 'grid_img')

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'image': forms.TextInput(attrs={'class': 'form-control'}),
        'country': forms.TextInput(attrs={'class': 'form-control'}),
        'grid_img': forms.TextInput(attrs={'class': 'form-control'}),
    }

# class RegisterUserForm(UserCreationForm):
