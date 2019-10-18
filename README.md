# skill general

## 功能
  登录注册接口
  各种crud接口  
  ES索引crud接口  
  登录校验中间件  
  DRF序列化  
  channels聊天  
  rpc远程调用  
  celery使用  
  gunicorn、uwsgi  
  supervisor  
  内存跟踪装饰器


## 服务启动

uwsgi启动方式：首先进入虚拟环境，然后再执行
`
uwsgi --ini server.ini
`

  或者命令行方式启动：
`
uwsgi --http :8001 --chdir /home/python/gitproject/skill-general/career --wsgi-file settings/wsgi.py --master --processes 4 --threads 2 --home /home/python/virtualenvs/django_career
`  
  
  gunicorn启动方式：  
  方式1：`gunicorn -w 4 -b 192.168.0.103:8000 settings.wsgi:application`    
  方式2：`gunicorn settings.wsgi:application -c gunicorn.ini`    
  方式3：`sh gunicorn.sh start`    `sh gunicorn.sh stop`
