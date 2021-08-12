####################
#urls.py用來寫網頁的網址
#透過url.py設定頁面的路徑(127.0.0.1/index)
#####################

from django.urls import path
from . import views

urlpatterns =  [
    path('',views.index,name='index'),
]