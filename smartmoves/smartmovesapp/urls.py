from django.urls import path
from .views import home_page, upload_resume_view, submit_resume_view

urlpatterns = [
    path('/', home_page),
    path('/uploadResume', upload_resume_view),
    path('/submitResume', submit_resume_view)
]
