# 登录验证
from django.http import HttpResponseRedirect


# 登录验证
def login_check(fn):
    def wrap(request, *args, **kwargs):
        if 'uname' not in request.session or 'uid' not in request.session:
            c_uname = request.COOKIES.get('uname')
            c_uid = request.COOKIES.get('uid')
            if not c_uname or not c_uid:
                return HttpResponseRedirect('/user/login')
            else:
                # cookie存在,回写session
                request.session['uname'] = c_uname
                request.session['uid'] = c_uid
        return fn(request, *args, **kwargs)

    return wrap
