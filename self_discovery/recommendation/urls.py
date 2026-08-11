from django.urls import path
from .views import (
    home,
    about_page,
    job_recommendation,
    predict_job,
    roadmap_page,
    resources_page,
    team_page,
    contact_page,
    admin_page,
    chatbot_page
    
)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about_page, name='about_page'),
    path('job-recommendation/', job_recommendation, name='job_recommendation'),
    path('predict/', predict_job, name='predict_job'),
    path('roadmap/', roadmap_page, name='roadmap_page'),
     path('resources/', resources_page, name='resources_page'),
    path('team/', team_page, name='team_page'),
    path('contact/', contact_page, name='contact_page'),
    path('admin-page/', admin_page, name='admin_page'),
    path('career-assistant/', chatbot_page, name='chatbot_page'),]
