from django.shortcuts import render
from portfolio.models import Project

# Create your views here.
def home(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    
    return render(request, 'portfolio/home.html', context)

def project_detail(request, pk):
    projects = Project.objects.get(pk=pk)
    context = {
        'projects': projects
    }
    
    return render(request, 'portfolio/project_detail.html', context)

# def base(request):
#     return render(request, 'portfolio/base.html')