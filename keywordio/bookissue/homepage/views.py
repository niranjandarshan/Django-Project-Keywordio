from django.shortcuts import render

# Create your views here.
def homepageaction(request):
    
        return render(request,'homepage_page.html')
