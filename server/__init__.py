import os

from flask import Flask


def create_flask_app():
    """
    初始化flask app settings
    :return:
    """
    from .settings import AppDefaultSetting, AppProductionSettings

    if os.environ.get("FLASK_ENV") == "production":
        settings = AppProductionSettings
    else:
        settings = AppDefaultSetting

    app = Flask(import_name=settings.APP_NAME,
                static_url_path='/',
                static_folder=os.path.join(settings.BASE_DIR, 'resources'),
                template_folder=os.path.join(settings.BASE_DIR, 'resources'),
                root_path=settings.BASE_DIR)

    app.config.from_object(settings)

    # 希望环境变量FLASK_DEBUG重载DEBUG
    env_debug = os.environ.get("FLASK_DEBUG")
    if env_debug == "False" or env_debug == "false":
        app.config['DEBUG'] = False

    print('ENV: {}'.format(app.config.get('ENV')))
    print('DEBUG: {}'.format(app.debug))

    return app


def create_web_app():
    """
    初始化本网站web_app
    :return: flask_app
    """
    app = create_flask_app()

    # 防止csrf攻击
    from flask_wtf.csrf import CSRFProtect
    CSRFProtect(app)

    # init mysql
    import pymysql
    pymysql.install_as_MySQLdb()

    # 数据库
    from .models import db
    db.init_app(app)
    app.db = db

    # 缓存
    from flask_caching import Cache
    app.cache = Cache(app)

    # Admin
    from flask_admin import Admin
    from flask_admin.contrib.sqla import ModelView
    from .models import Mailbox
    from flask_babelex import Babel
    admin = Admin(app, name='About Me Admin', template_mode='bootstrap3')
    admin.add_view(ModelView(Mailbox, app.db.session))
    Babel(app)

    # email
    from smtplib import SMTP
    host = app.config.get("EMAIL_HOST")
    account = app.config.get("EMAIL_ACCOUNT")
    password = app.config.get("EMAIL_PASSWORD")
    smtp = SMTP(host, 25)
    smtp.login(account, password)
    app.smtp = smtp

    return app



