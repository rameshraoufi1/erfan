from django.shortcuts import render,redirect
from . models import *
from django.core.mail import send_mail
from django.conf import settings
from .forms import *

# Create your views here.


def index(request):
    desc = Home.objects.all()
    home_services = HomeServices.objects.all()
    home_discover = HomeDiscover.objects.all()
    home_blog = HomeBlog.objects.all()
    context = {'desc':desc,'home_services':home_services,'home_discover':home_discover,'home_blog':home_blog}
    return render(request,'index.html',context)


def about_us(request):
    about = AboutUs.objects.all()
    projects = AboutUsProjects.objects.all()
    context = {'about':about,'projects':projects}
    return render(request, 'about-us.html',context)


def services_1(request):
    services = Services.objects.all()
    service_gallery = ServicesGallery.objects.all()
    context = {'services':services,'service_gallery':service_gallery}
    return render(request, 'services-1.html',context)


def services_2(request):
    return render(request, 'services-2.html')


def carpet_rugs(request):
    return render(request, 'carpets-rugs.html')

def our_history(request):
    return render(request, 'our-history.html')

def our_team(request):
    our_team = Our_Team.objects.all()
    context = {'our_team':our_team}
    return render(request, 'our-team.html',context)

def portfolio_single(request):
    portfolio = Portfolio.objects.all()
    context = {'portfolio':portfolio}
    return render(request, 'portfolio-single.html',context)

def our_blog(request):
    return render(request, 'our-blog.html')

def contact_us(request):
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form':form}
    return render(request, 'contact-us.html',context)

def laminate_flooring(request):
    return render(request, 'laminate-flooring.html')

def in_home_choose_a_light_floor_if_at_all_possible(request):
    return render(request, 'in-home-choose-a-light-floor-if-at-all-possible.html')

def laminate_flooring(request):
    return render(request, 'laminate-flooring.html')