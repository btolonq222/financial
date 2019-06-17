from django.contrib import admin
from article.models import Article, Comment

class CommentModelAdmin(admin.ModelAdmin): #增加一個CommentModelAdmin類別(繼承admin.ModelAdmin)
    list_display = ['article', 'content', 'pubDateTime']  #客製化頁面顯示清單(list_display)：顯示article與content欄位
    list_display_links = ['article']  #設定資料連接欄位(list_display_links)：透過article來連結(此項為預設)
    list_filter = ['article', 'content'] #設定過濾器(list_filter)：設定右方過濾欄位為article與content，點選即可濾出該項目的有關資料
    search_fields = ['content'] #設定搜尋欄位(search_fields)：設定搜尋欄位為content，輸入資料即可搜尋該欄位的內容
    list_editable=['content'] #設定編輯欄位(list_editable)：設定content欄位可編輯
    
    
    
    
    class meta:   #一個類別容器(Class container)內含有該類別的詮釋資料(metadata)，例如：排序、權限、所使用的Model等
        model = Comment
    

admin.site.register(Article)
admin.site.register(Comment,CommentModelAdmin)
# Register your models here.
