# skill general

uwsgi启动方式：首先进入虚拟环境，然后再执行
`
uwsgi --ini server.ini
`

  或者命令行方式启动：
`
uwsgi --http :8001 --chdir /home/python/gitproject/skill-general/career --wsgi-file settings/wsgi.py --master --processes 4 --threads 2 --home /home/python/virtualenvs/django_career
`
