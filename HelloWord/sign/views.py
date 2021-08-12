############################
#views.py用來撰寫每個網頁的內容
#透過view.py設定視圖(顯示hello Louis)
############################

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''
def index(request):
    return HttpResponse("Hello,Louis.")
'''
def index(request):
    return render(request,"index.html") #將index.html頁面拋給使用者