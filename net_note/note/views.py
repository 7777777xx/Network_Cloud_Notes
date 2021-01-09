import html

from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Note
from tools.login_check import login_check


# Create your views here.


# 显示笔记列表
@cache_page(10)
@login_check
def list_view(request):
    uname = request.session['uname']
    uid = request.session['uid']
    print(uid)
    try:
        notes = Note.objects.filter(user_id=uid)
        paginator = Paginator(notes, 1)
        cur_page = request.GET.get('page', 1)  # 得到默认的当前页
        page = paginator.page(cur_page)
        print('11111 %s' % notes)
    except Exception as e:
        print('error is %s' % e)

    return render(request, 'note/list_note.html', locals())


# 添加笔记
@login_check
def add_view(request):
    if request.method == 'GET':
        return render(request, 'note/add_note.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        # 转义
        title = html.escape(title)
        content = html.escape(content)

        uid = request.session['uid']
        Note.objects.create(title=title, content=content, user_id=uid)
        return HttpResponseRedirect('/note/')


# 修改笔记
@login_check
def mod_view(request, id):
    try:
        note = Note.objects.get(id=id)
    except Exception as e:
        print('error is %s ' % e)
        return HttpResponse('未找到该笔记!')
    if request.method == 'GET':
        return render(request, 'note/mod_note.html', locals())
    elif request.method == 'POST':
        new_title = request.POST.get('title')
        new_content = request.POST.get('content')
        note.title = new_title
        note.content = new_content
        note.save()
        return HttpResponseRedirect('/note/')


# 删除笔记
@login_check
def del_view(request, id):
    try:
        note = Note.objects.get(id=id)
        note.delete()
    except Exception as e:
        print('error is %s ' % e)
        return HttpResponse('未找到该笔记!')
    return HttpResponseRedirect('/note/')
