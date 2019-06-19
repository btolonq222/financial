from django.shortcuts import render
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
