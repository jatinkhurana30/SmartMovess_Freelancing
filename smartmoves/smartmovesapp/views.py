from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, 'index.html')


def upload_resume_view(request):
    return render(request, 'uploadResume.html')

def submit_resume_view(request):
    return render("DOne")
