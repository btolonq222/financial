from populate import admin, users, article

admin.populate()
users.populate()
article.populate()

#由於local.py模組一定是直接被執行的，不會被匯入，所不需判斷(if __name__=="__main__")。