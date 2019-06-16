from django.shortcuts import render


def article(request):
    """
    Render the page
    """
    return render(request, 'article/article.html')
# Create your views here.
