from flask import render_template, request, current_app, send_from_directory
import re
from multiprocessing import Process

from . import create_web_app, constants
from .models import Mailbox
from .utils import send_leave_word

app = create_web_app()


@app.route('/')
def index():
    """
    首页视图
    :return:
    """
    return render_template('index.html',
                           resume_url='/download/{}'.format(constants.RESUME_FILE_NAME),
                           blog_link=constants.BLOG_LINK)


@app.route('/employ')
def employ():
    """
    雇用视图
    :return:
    """
    return render_template('employ.html')


@app.route('/help', methods=['POST'])
def my_help():
    """
    处理How Can I Help
    :return:
    """
    form = request.form
    ip = request.remote_addr

    username = form.get('username', '')
    email = form.get('email', '')
    subject = form.get('subject', '')
    phone = form.get('phone')
    message = form.get('message', '')

    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        # 邮箱格式错误
        return {'message': '邮箱模式错误'}, 400

    if phone:
        if not re.match(r"^1[3-9]\d{9}$", str(phone)) \
                and not re.match(r'^\d{3}-\d{8}|\d{4}-\d{7}$', str(phone)):
            # 号码错误
            return {'message': '号码格式错误'}, 400

    # 防止频繁发送
    pv = current_app.cache.get(ip) or 0
    if pv > 0:
        return {'message': '请勿频繁发送!'}, 403

    # 记录ip
    current_app.cache.set(ip, pv, timeout=constants.USER_SUBMIT_HELP_TIMEOUT)

    # 保存数据
    mailbox = Mailbox(name=username, phone=phone, email=email, subject=subject, message=message)
    current_app.db.session.add(mailbox)
    current_app.db.session.commit()

    # send_leave_word(mailbox=mailbox, smtp=current_app.smtp)
    try:
        Process(target=send_leave_word, kwargs={"mailbox": mailbox, "smtp": current_app.smtp}).start()
        return {'message': '感谢! 您请求的内容我已收到.'}
    except Exception as e:
        return {'message': '抱歉, 邮件系统出错~~ 请通过微信等方式联系我\n'
                           'Exception: {}'.format(e)}


@app.route('/download/<file_name>')
def download(file_name):
    """下载文件"""
    return send_from_directory(current_app.static_folder, file_name)


@app.route('/status')
def status():
    return {"DEBUG": current_app.config.get('DEBUG'),
            "ENV": current_app.config.get("ENV")}

