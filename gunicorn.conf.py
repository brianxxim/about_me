bind = '127.0.0.1:26381'
workers = 1
threads = 2
# 重载/当代码变动时自动重启
reload = True
daemon = False
# 工作模式
worker_class = 'gevent'
# 单进程最大并发(针对gevent模式)
# worker_connections = 2048

# ssl密钥
keyfile = '/home/brianblog.asia.key'
# ssl证书
certfile = '/home/brianblog.asia_bundle.crt'

# 设置进程文件目录
pidfile = './gunicorn.pid'
# 设置访问日志和错误信息日志路径
accesslog = './logs/gunicorn_access.log'
errorlog = './logs/gunicorn_error.log'
# 设置日志记录水平
loglevel = 'warning'
