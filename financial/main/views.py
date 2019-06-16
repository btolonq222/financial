from django.shortcuts import render



def main(request):
    """
    Render the main page
    """
    return render(request, 'main/main.html')

def about(request):
    """
    Render the main page
    """
    return render(request, 'main/about.html')
# Create your views here.
