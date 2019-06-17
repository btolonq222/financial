from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=128, unique=True)
    content = models.TextField()
    pubDatetime = models.DateTimeField(auto_now_add=True)  #DateTimeFiled 日期時間格式 
    def __str__(self):                                     #auto_now_add=True 在物件新增時自動設定為當時時間，設定之後即無法修改
        return self.title
    
    class meta:
        ordering = ['-pubDateTime']  #物件存入資料庫時依照時間反向排序(負值表示反向)，此處使用pythonlist資料結構來指定欄位，並可設定多個欄位排序

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=128)
    pubDateTime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.article.title + '-' + str(self.id)
    
    class meta:
        ordering = ['-pubDateTime']