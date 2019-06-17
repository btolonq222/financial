from populate import base
from article.models import Article, Comment

titles = ['如何像電腦科學家一樣思考', '10分鐘內學好Python', '簡單學習Django']
comments = ['文章真棒', '並不認同您的觀點', '借分享', '學好一個程式語言或框架並不容易']

def populate():
    print('Populating articles and comments ...', end='')
    Article.objects.all().delete()   #刪除所有文章
    Comment.objects.all().delete()   #刪除所有留言
    
    for title in titles:
        article = Article()   #創造一個Article實體
        article.title = title
        for j in range(20):
            article.content += title +'\n'
        article.save()
        for comment in comments:
            Comment.objects.create(article=article, content=comment) #新增並儲存此文章所屬留言，每個文章儲存4筆留言
    print('Done!!!')
    
    
if __name__ == '__main__':   #如果此模組是直接執行而不是被匯入，就呼叫populate()函式來新增資料。
    populate()
    """
    PYthon模組的執行與匯入：
      1.模組被直接執行時，Python會將內建變數__name__內容設定為__main__. 
      2.模組被匯入時，python會將__name__設定為該模組名稱，例如：
          import math
          print(math.__name__)
          >>>math
                     因此判斷__name__變數，就可以知道該模組是直接或是被匯入。
    
    """
    