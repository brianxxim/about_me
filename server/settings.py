import os
from urllib import parse


class AppDefaultSetting(object):
    """
    程序配置
    """
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    SECRET_KEY = '1+Lkj7wfnA6WeMKbKyu*8ndBGbMG2h!eW3zmeBurw7L_g+ISrbte@11MSB$yfuyG'
    ENV = 'development'
    DEBUG = True

    # 数据库
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./data.db'
    # SQLALCHEMY_DATABASE_URI = r'mysql://root:{}@mysqlbrianblog.mysql.database.azure.com:3306/about_me'.format(parse.quote_plus("KAka5977$"))
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # 是否追踪数据修改
    SQLALCHEMY_ECHO = True  # 显示生成的SQL语句，可用于调试

    # 缓存
    # CACHE_TYPE = 'FileSystemCache'
    # CACHE_DIR = os.path.join(BASE_DIR, 'caches')
    CACHE_TYPE = 'SimpleCache'
    CACHE_DEFAULT_TIMEOUT = 1

    # 邮箱
    EMAIL_ACCOUNT = "brianblogger@163.com"
    # Mail from must equal authorized user
    # EMAIL_FROM_ADDR = "chengrip@foxemail.com"
    EMAIL_PASSWORD = "JZLOMNAQNREZQCCW"
    EMAIL_HOST = "smtp.163.com"

    # admin
    BABEL_DEFAULT_LOCALE = 'zh_CN'

    # 是否通过检查 referrer 是否与主机匹配来执行同源策略。仅适用于 HTTPS 请求。默认为True
    WTF_CSRF_SSL_STRICT = False

    APP_NAME = 'about_me'


class AppProductionSettings(AppDefaultSetting):
    """
    程序配置(生产环境)
    """
    CACHE_DEFAULT_TIMEOUT = 60 * 5
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    ENV = 'production'
    DEBUG = False  # 由环境变量FLASK_DEBUG重载
