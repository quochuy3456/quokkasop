from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request, 'Qk_Template_Home/home.html')


def home_page2(request):
    return render(request, 'Qk_Template_Home/home2.html')
