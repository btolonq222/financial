from populate import base
from django.contrib.auth.models import User




def populate():
    print('Creating user accounts...', end='')
    User.objects.exclude(is_superuser=True).delete() #除了管理者外，清除所有使用者帳號
    for i in range(5):
        username='user' + str(i)
        User.objects.create_user(username=username, email=None, password=username) #利用create_user()函式新增使用者帳號
    print('Done!!')
    
    
    
if __name__ == "__main__":
    populate()