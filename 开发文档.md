#  开发文档

## 项目信息

```
项目名称:网络云笔记
项目时间:2021.01.04-2021.01.6
项目人员:七xx
项目描述:该项目是学习Python过程中以实现在线笔记为目的而设计，使用的是Python中的Django框架，采用的是MTV模式开发的web项目，目前由用户模块，笔记模块组成，已实现登陆注册退出 ，查看笔记列表，创建新笔记，修改笔记，删除笔记等功能。

```



## 开发规范

```
开发环境:Windows 10 + Python 3.8 + Mysql 8.0.22 + Pycharm + Git
```



## 功能模块

```
用户模块:
	1. 注册
    2. 登陆
    3. 退出登陆
    
笔记模块:
	1.查看笔记列表
    2. 创建新笔记
    3. 修改笔记
    4. 删除笔记

```



## 数据库设计

```
数据库:Net_Note
create database Net_Note default charset utf8;
```



- 模型类

```
用户模型类:User
class User(models.Model):
    username = models.CharField("用户名", max_length=30, unique=True)
    password = models.CharField("密码", max_length=32)
	created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return "用户" + self.username
```

|     字段     | 字段类型 |   作用   |   备注   |
| :----------: | :------: | :------: | :------: |
|   username   | char(30) |  用户名  |   唯一   |
|   password   | char(32) |   密码   | 加密存储 |
| create_time  | datetime | 创建时间 |          |
| updated_time | datetime | 更新时间 |          |



```
笔记模型类:Note
class Note(models.Model):
    title = models.CharField('标题', max_length=100)
    content = models.TextField('内容')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)
	user = models.IntegerField(User, on_delete=models.CASCADE)
```

|    字段名    | 字段类型  |   作用   | 备注 |
| :----------: | :-------: | :------: | :--: |
|    title     | char(100) |   标题   |      |
|   content    |   text    |   内容   |      |
| created_time | datetime  | 创建时间 |      |
| updated_time | datetime  | 修改时间 |      |
|   user_id    |    int    |  用户id  |      |

## 设计规范

- 主页设计规范

	|  路由   |  视图函数  |          模板位置          | 说明 |
	| :-----: | :--------: | :------------------------: | :--: |
	| /index/ | index_view | templates/index/index.html | 主页 |

- 登录注册退出设计规范

	|     路由     |  视图函数   |           模板位置           | 说明 |
	| :----------: | :---------: | :--------------------------: | :--: |
	| /user/login  | login_view  |  templates/user/login.html   | 登陆 |
	|  /user/reg   |  reg_view   | templates/user/register.html | 注册 |
	| /user/logout | logout_view |         无(返回首页)         | 退出 |

- 笔记设计规范

	|      路由       | 视图函数  |           模板位置            |       说明       |
	| :-------------: | :-------: | :---------------------------: | :--------------: |
	|     /note/      | list_view | templates/note/list_note.html | 显示笔记列表功能 |
	|    /note/add    | add_view  | templates/note/add_note.html  |    添加云笔记    |
	| /note/mod/(\d+) | mod_view  | templates/note/mod_note.html  |  修改之前云笔记  |
	| /note/del/(\d+) | del_view  |        无(返回列表页)         |    删除云笔记    |

	

## 待优化

```
1.添加前端模板css样式
2.将项目进行前后端分离设计
3.利用JWT生成token令牌
4.添加短信验证模块
5.添加前后端正则验证模块

```

