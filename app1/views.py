from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request,'app1/mainpage.html')
