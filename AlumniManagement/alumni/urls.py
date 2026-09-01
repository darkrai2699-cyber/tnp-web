from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.alumni_login, name='alumni_login'),
    path('register/', views.alumni_registration, name='alumni_registration'),
    path('coordinator-login/', views.alumni_coordinator_login, name='alumni_coordinator_login'),
    path('mentor-login/', views.batch_mentor_login, name='batch_mentor_login'),
    path('gallery/', views.gallery, name='gallery'),
    path('about-us/', views.about_us, name='about_us'),
    path('event/<int:event_id>/download/', views.download_event_media, name='download_event_media'),
    path('api/visitor_count/', views.visitor_count_api, name='visitor_count_api'),
    path('profile/', views.alumni_profile, name='alumni_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('mentor/dashboard/', views.mentor_dashboard, name='mentor_dashboard'),
    path('coordinator/dashboard/', views.coordinator_dashboard, name='coordinator_dashboard'),
    path('logout/', views.logout_view, name='logout'),
]
