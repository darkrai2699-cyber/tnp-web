import uuid
from django import forms
from django.contrib.auth.hashers import make_password
from .models import Alumni, Event, GalleryPhoto, BatchMentor


class AlumniRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Create a secure password (min 6 characters)',
            'id': 'reg_password',
            'required': True,
        }),
        help_text="Password must be at least 6 characters."
    )

    class Meta:
        model = Alumni
        exclude = ['id', 'is_superuser', 'last_login', 'groups', 'user_permissions', 'is_top_alumni', 'is_active', 'is_staff']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Rahul Sharma', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'e.g. rahul.sharma@example.com', 'required': True}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. +91 9876543210'}),
            'graduation_year': forms.NumberInput(attrs={'class': 'form-control', 'min': 1980, 'max': 2030, 'placeholder': 'e.g. 2022', 'required': True}),
            'sector': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Information Technology / Telecommunications'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': 'Years of experience'}),
            'current_job_profile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Senior Software Engineer'}),
            'current_company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Tata Consultancy Services'}),
            'current_job_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Pune, Maharashtra'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City', 'required': True}),
            'sub_district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Taluka / Sub-district'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'District', 'required': True}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State', 'required': True}),
            'pincode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pincode', 'required': True}),
            'is_international': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country (if outside India)'}),
            'full_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Complete residential address', 'required': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Brief bio or professional summary (optional)'}),
            'profile_photo': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*', 'id': 'profilePhotoInput'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://linkedin.com/in/username'}),
            'github': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://github.com/username'}),
            'facebook': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://facebook.com/username'}),
            'instagram': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://instagram.com/username'}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.password = make_password(instance.password)
        if not instance.id:
            instance.id = str(uuid.uuid4())[:8]
        if commit:
            instance.save()
        return instance


class AlumniProfileForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = [
            'current_job_profile',
            'current_company',
            'current_job_location',
            'city',
            'sub_district',
            'district',
            'state',
            'pincode',
            'is_international',
            'country',
            'full_address',
            'description',
            'profile_photo',
            'facebook',
            'github',
            'instagram',
            'linkedin',
        ]
        widgets = {
            'current_job_profile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Lead System Architect'}),
            'current_company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Cisco Systems'}),
            'current_job_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Bangalore, India'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'sub_district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sub-district'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'District'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pincode'}),
            'is_international': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'full_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Full Address'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Bio / Career Summary'}),
            'profile_photo': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*', 'id': 'profilePhotoInput'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://linkedin.com/in/username'}),
            'github': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://github.com/username'}),
            'facebook': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://facebook.com/username'}),
            'instagram': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://instagram.com/username'}),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'media', 'date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Title', 'required': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Event Description', 'required': True}),
            'media': forms.FileInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': True}),
        }


class GalleryPhotoForm(forms.ModelForm):
    class Meta:
        model = GalleryPhoto
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Photo Title', 'required': True}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'required': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Short caption / description'}),
        }


class BatchMentorForm(forms.ModelForm):
    class Meta:
        model = BatchMentor
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mentor Full Name'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'profile_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'assigned_batches': forms.SelectMultiple(attrs={'class': 'form-select', 'size': '5'}),
        }
