from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    """Render the home page."""
    return render(request, 'index.html')




# About page





#Services page

def portfolio(request):
    return render(request, "portfolio.html")






# menu page

def blog(request):
    return render(request, "blog.html")


# def contact(request):
#     return render(request, "contact.html")


from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Profile  # Make sure this is imported

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()

    profile = Profile.objects.first()  # Same as index view

    return render(request, 'contact.html', {
        'form': form,
        'profile': profile
    })



from django.shortcuts import render
from .models import  Service, Testimonial

from .models import Service, Testimonial, Profile

def index(request):
    services = Service.objects.all()
    testimonials = Testimonial.objects.all().order_by('-date')
   
    profile = Profile.objects.first()  # or filter by user if needed

    return render(request, 'index.html', {
        'services': services,
        'testimonials': testimonials,
        
        'profile': profile
    })


from django.shortcuts import render
from .models import Skill, Profile  # Add Profile here

def resume(request):
    skills = Skill.objects.all()
    profile = Profile.objects.first()  # Assuming only 1 profile (admin)
    return render(request, 'resume.html', {
        'skills': skills,
        'profile': profile
    })

