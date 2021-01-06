from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# 主页
def index_view(request):

    if 'uname' not in request.session or 'uid' not in request.session:

        if not request.COOKIES.get('uname') or not request.COOKIES.get('uid'):
            uname = ' '

        else:
            uname = request.COOKIES.get('uname')
    else:
        uname = request.session.get('uname')
    return render(request, 'index/index.html', locals())



