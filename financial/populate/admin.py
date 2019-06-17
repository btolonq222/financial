from populate import base
from django.contrib.auth.models import User


def populate():
    print('Creating admin account ...', end='')
    User.objects.all().delete()   #清除所有User Model裡的資料
    User.objects.create_superuser(username='admin', email=None, password='admin') #利用create_superuser()函式新增admin帳號
    print('Done!!!')
    
    
if __name__=='__main__':
    populate()
    