from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import User
import hashlib


# Create your views here.


# 登录
def login_view(request):
    if request.method == "GET":
        # 判断用户是否登录过
        if 'uname' in request.session and 'uid' in request.session:
            return HttpResponseRedirect('/note/')
        # 判断cookie中是否有数据
        uname = request.COOKIES.get('uname')
        uid = request.COOKIES.get('uid')
        if uname and uid:
            # 将cookie数据回写session
            request.session['uname'] = uname
            request.session['uid'] = uid

            # 免登录
            return HttpResponseRedirect('/note/')


        return render(request, 'user/login.html')



    elif request.method == "POST":

        # 打印表单数据
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 为空判断
        if not username or not password:
            return HttpResponse('用户名和密码不能为空')
        # 检查用户是否存在
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            print('error is %s ' % e)
            return HttpResponse('用户名或密码错误!')
        # 检查密码
        md5 = hashlib.md5()
        md5.update(password.encode())
        password_h = md5.hexdigest()
        if password_h != user.password:
            return HttpResponse('用户名或密码错误!')

        # 在session保存用户信息
        request.session['uname'] = user.username
        request.session['uid'] = user.id
        # 在cookie中也保存用户信息
        resp = HttpResponseRedirect('/note/')
        if 'remember' in request.POST:
            resp.set_cookie('uname', user.username, 7*3600*24)
            resp.set_cookie('uid', user.id, 7*3600*24)

        return resp




# 注册
def reg_view(request):
    if request.method == "GET":
        return render(request, 'user/register.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')

        # 为空验证
        if not username or not password_1:
            return HttpResponse('用户名或密码不能为空')
        # 两次密码一致验证
        if password_1 != password_2:
            return HttpResponse('两次密码不一致!')
        # 用户名唯一验证
        old_uname = User.objects.filter(username=username)
        if old_uname:
            return HttpResponse('用户名已存在!')
        # 密码加密
        md5 = hashlib.md5()
        md5.update(password_2.encode())
        password_h = md5.hexdigest()

        # 添加数据
        try:
            User.objects.create(username=username,
                                password=password_h)
        except Exception as e:
            print('error is %s ' % e)
            return HttpResponse('用户名已存在!')

        return HttpResponseRedirect('/user/login')


# 退出
def logout_view(request):
    # 清除session
    if 'uname' in request.session:
        del request.session['uname']
    if 'uid' in request.session:
        del request.session['uid']
    # 清除COOKIE
    resp = HttpResponseRedirect('/index/')
    if 'uname' in request.COOKIES:
        resp.delete_cookie('uname')
    if 'uid' in request.COOKIES:
        resp.delete_cookie('uid')
    return resp
