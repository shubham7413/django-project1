from django.contrib import admin
from django.urls import path, include
from home import views

#Django admin header customization
admin.site.site_header = "Developer Shubham"
admin.site.site_title = "Welcome to Shubham Dashboard"
admin.site.index_title = "Welcome to this Portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.project, name='project'),
    path('contact', views.contact, name='contact'),
]
