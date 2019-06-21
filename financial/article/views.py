from django.shortcuts import render

from article.forms import ArticleForm
from article.models import Article, Comment


def article(request):
    """
    Render the page
    """
    articles = {} 
    for article in Article.objects.all():
        articles.update({article:Comment.objects.filter(article=article)})
    context = {'articles':articles}   #利用範本變數articles將查詢結果傳至範本
    
    return render(request, 'article/article.html', context)
# Create your views here.


def articleCreate(request):
    """
    Create a new article instance
    1. if method is GET, render an empty form
    2. if methond is POST, perform form validation and display error messages if the form is invalid
    3. save the form to the model and redirect the user to the aritcle page
    """
    template = 'article/articleCreate.html'
    if request.method =='GET':
        return render(request, template, {'articleForm':ArticleForm()})