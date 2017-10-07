from django.shortcuts import render

def index(request):
    return render(request, 'info/1.html')
def about(request):
    return render(request, 'info/about.html')
def contact(request):
    return render(request, 'info/2.html')
