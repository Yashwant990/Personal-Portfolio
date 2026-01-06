# portfolio/Base/urls.py

from django.urls import path
from . import views # Import the views module from the same directory

# App namespace is often useful but not strictly needed for this simple setup
# app_name = 'Base' 

urlpatterns = [
    # Maps the root path received from the project URLconf ('/') to the 'home' view
    path('', views.home, name='home'),
    path('About.html', views.about, name='about'),
    
    path('Projects.html', views.projects, name='projects'),
    path('Contact.html', views.contact, name='contact'),
]