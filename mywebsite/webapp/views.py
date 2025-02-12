from django.shortcuts import render

def index(request):
    return render(request, 'webapp/index.html')

def resume(request):
    return render(request, 'webapp/resume.html')

def projects(request):
    return render(request, 'webapp/projects.html')

def contact(request):
    return render(request, 'webapp/contact.html')

