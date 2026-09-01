import os
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, FileResponse
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.db.models import Q, Count
from .models import *
from .forms import *


def index(request):
    events = Event.objects.all().order_by('-date')
    top_alumni = Alumni.objects.filter(is_top_alumni=True)
    if not top_alumni.exists():
        # Fallback to recent alumni if none marked as top
        top_alumni = Alumni.objects.all().order_by('-graduation_year')[:8]
    photos = GalleryPhoto.objects.all()
    visitor, _ = VisitorCount.objects.get_or_create(id=1)
    
    # Stats for counter section
    total_alumni_count = Alumni.objects.count()
    total_events_count = Event.objects.count()
    total_mentors_count = BatchMentor.objects.count()
    
    context = {
        'events': events,
        'top_alumni': top_alumni,
        'photos': photos,
        'visitor_count': visitor.count,
        'total_alumni': max(total_alumni_count, 500),
        'total_events': max(total_events_count, 100),
        'total_mentors': max(total_mentors_count, 25),
    }
    return render(request, 'index.html', context)


def alumni_login(request):
    if request.session.get('alumni_id'):
        return redirect('alumni_profile')
        
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        try:
            alumni = Alumni.objects.get(email=email)
            if check_password(password, alumni.password) or alumni.password == password:
                request.session['alumni_id'] = alumni.id
                request.session['user_role'] = 'alumni'
                request.session['user_name'] = alumni.full_name
                messages.success(request, f"Welcome back, {alumni.full_name}!")
                return redirect('alumni_profile')
        except Alumni.DoesNotExist:
            pass
        return render(request, 'alumni/login.html', {'error': 'Invalid email address or password. Please try again.'})
    return render(request, 'alumni/login.html')


def alumni_registration(request):
    if request.method == 'POST':
        form = AlumniRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            alumni = form.save()
            messages.success(request, f"Registration successful for {alumni.full_name}! Please sign in with your credentials.")
            return redirect('alumni_login')
        else:
            messages.error(request, "Please correct the highlighted errors in the registration form.")
    else:
        form = AlumniRegistrationForm()
    return render(request, 'alumni/registration.html', {'form': form})


def alumni_coordinator_login(request):
    if request.session.get('coordinator_id'):
        return redirect('coordinator_dashboard')
        
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        try:
            coordinator = AlumniCoordinator.objects.get(email=email)
            if coordinator.password == password or check_password(password, coordinator.password):
                request.session['coordinator_id'] = coordinator.id
                request.session['user_role'] = 'coordinator'
                request.session['user_name'] = coordinator.name
                messages.success(request, f"Welcome to the Coordinator Console, {coordinator.name}!")
                return redirect('coordinator_dashboard')
        except AlumniCoordinator.DoesNotExist:
            pass
        return render(request, 'alumni/coordinator_login.html', {'error': 'Invalid coordinator credentials.'})
    return render(request, 'alumni/coordinator_login.html')


def batch_mentor_login(request):
    if request.session.get('mentor_id'):
        return redirect('mentor_dashboard')
        
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        try:
            mentor = BatchMentor.objects.get(username=username)
            if mentor.password == password or check_password(password, mentor.password):
                request.session['mentor_id'] = mentor.id
                request.session['user_role'] = 'mentor'
                request.session['user_name'] = mentor.full_name
                messages.success(request, f"Welcome back, Prof./Dr. {mentor.full_name}!")
                return redirect('mentor_dashboard')
        except BatchMentor.DoesNotExist:
            pass
        return render(request, 'alumni/mentor_login.html', {'error': 'Invalid mentor username or password.'})
    return render(request, 'alumni/mentor_login.html')


def gallery(request):
    photos = GalleryPhoto.objects.all()
    return render(request, 'alumni/gallery.html', {'photos': photos})


def about_us(request):
    return render(request, 'alumni/about_us.html')


def download_event_media(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if event.media:
        file_path = event.media.path
        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'), as_attachment=True)
    return HttpResponse('File not found', status=404)


def visitor_count_api(request):
    visitor, _ = VisitorCount.objects.get_or_create(id=1)
    return JsonResponse({'visitor_count': visitor.count})


def alumni_profile(request):
    alumni_id = request.session.get('alumni_id')
    if not alumni_id:
        return redirect('alumni_login')
    alumni = get_object_or_404(Alumni, id=alumni_id)
    return render(request, 'alumni/profile.html', {'alumni': alumni})


def edit_profile(request):
    alumni_id = request.session.get('alumni_id')
    if not alumni_id:
        return redirect('alumni_login')
    alumni = get_object_or_404(Alumni, id=alumni_id)
    if request.method == 'POST':
        form = AlumniProfileForm(request.POST, request.FILES, instance=alumni)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('alumni_profile')
        else:
            messages.error(request, "Please check the form values.")
    else:
        form = AlumniProfileForm(instance=alumni)
    return render(request, 'alumni/edit_profile.html', {'form': form, 'alumni': alumni})


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        user_exists = Alumni.objects.filter(email=email).exists()
        return render(request, 'alumni/forgot_password.html', {
            'submitted': True,
            'email': email,
            'user_exists': user_exists
        })
    return render(request, 'alumni/forgot_password.html')


def mentor_dashboard(request):
    mentor_id = request.session.get('mentor_id')
    if not mentor_id:
        return redirect('batch_mentor_login')
    mentor = get_object_or_404(BatchMentor, id=mentor_id)
    assigned_years = list(mentor.assigned_batches.values_list('year', flat=True))
    
    # Query parameters
    search_query = request.GET.get('q', '').strip()
    selected_year = request.GET.get('year', '').strip()
    
    mentees_qs = Alumni.objects.filter(graduation_year__in=assigned_years) if assigned_years else Alumni.objects.all()
    
    if selected_year:
        try:
            mentees_qs = mentees_qs.filter(graduation_year=int(selected_year))
        except ValueError:
            pass
            
    if search_query:
        mentees_qs = mentees_qs.filter(
            Q(full_name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(current_company__icontains=search_query) |
            Q(current_job_profile__icontains=search_query) |
            Q(city__icontains=search_query)
        )
        
    context = {
        'mentor': mentor,
        'mentees': mentees_qs,
        'assigned_years': assigned_years,
        'search_query': search_query,
        'selected_year': selected_year,
        'mentee_count': mentees_qs.count(),
    }
    return render(request, 'alumni/mentor_dashboard.html', context)


def coordinator_dashboard(request):
    coordinator_id = request.session.get('coordinator_id')
    if not coordinator_id:
        return redirect('alumni_coordinator_login')
    coordinator = get_object_or_404(AlumniCoordinator, id=coordinator_id)
    
    # Handle adding event from dashboard
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add_event':
            form = EventForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "New event posted successfully to the event board!")
                return redirect('coordinator_dashboard')
            else:
                messages.error(request, "Failed to create event. Please verify required fields.")
        elif action == 'delete_event':
            event_id = request.POST.get('event_id')
            if event_id:
                event = get_object_or_404(Event, id=event_id)
                event.delete()
                messages.success(request, "Event removed successfully.")
                return redirect('coordinator_dashboard')
    
    events = Event.objects.all().order_by('-date')
    alumni_list = Alumni.objects.all().order_by('-graduation_year', 'full_name')[:50]
    mentors = BatchMentor.objects.all()
    event_form = EventForm()
    
    # Stats
    total_alumni = Alumni.objects.count()
    top_alumni_count = Alumni.objects.filter(is_top_alumni=True).count()
    total_events = events.count()
    total_photos = GalleryPhoto.objects.count()
    
    context = {
        'coordinator': coordinator,
        'events': events,
        'alumni_list': alumni_list,
        'mentors': mentors,
        'event_form': event_form,
        'stats': {
            'total_alumni': total_alumni,
            'top_alumni': top_alumni_count,
            'total_events': total_events,
            'total_photos': total_photos,
        }
    }
    return render(request, 'alumni/coordinator_dashboard.html', context)


def logout_view(request):
    request.session.flush()
    messages.info(request, "You have been logged out safely.")
    return redirect('index')
