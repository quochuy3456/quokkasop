from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request, 'Qk_Template_Home/home.html')
