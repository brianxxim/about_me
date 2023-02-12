import os
from smtplib import SMTPException
from email.header import Header
from email.mime.text import MIMEText
from jinja2 import Template, Environment, PackageLoader, FileSystemLoader

from . import constants
from .settings import AppDefaultSetting


template_env = Environment(loader=FileSystemLoader(os.path.join(AppDefaultSetting.BASE_DIR, 'resources')))


def _verification_account(smtp):
    """
    校验smtp账号密码是否存在
    """
    text = str()
    user = getattr(smtp, "user", None)
    password = getattr(smtp, "password", None)

    if user is None:
        text += "未设置smtp.user\n"

    if password is None:
        text += "未设置smtp.password\n"

    if text:
        raise SMTPException(text + "建议使用smtp.login()设置")

    return user, password


def send_email(to_addrs, smtp, message):
    """
    发送邮件
    :return:
    """
    if not isinstance(to_addrs, list):
        to_addrs = [to_addrs]

    account, password = _verification_account(smtp)

    message_string = message.as_string()

    try:
        # smtp.login(account, password)
        smtp.sendmail(account, to_addrs, message_string)
    except SMTPException:
        try:
            smtp.login(account, password)
            smtp.sendmail(account, to_addrs, message_string)
        except SMTPException as e:
            print(e, "Error: 无法发送邮件")
            return False

    return True


def send_leave_word(smtp, mailbox):
    """
    发送留言
    :param smtp:
    :param mailbox:
    :return:
    """
    # 邮件主体
    html = template_env.get_template('email/leave_word.html')
    content = html.render(subject=mailbox.subject,
                          name=mailbox.name,
                          email=mailbox.email,
                          phone=mailbox.phone,
                          message=mailbox.message,
                          admin_link=constants.ADMIN_LINK
                          )

    message = MIMEText(content, 'html', 'utf-8')  # 内容
    message['From'] = Header("Brian <{}>".format(AppDefaultSetting.EMAIL_ACCOUNT), 'utf-8')  # 发件人抬头
    message['To'] = Header("BOSS", 'utf-8')  # 收件人名称
    message['Subject'] = Header('留言提醒', 'utf-8')  # 主题

    return send_email(mailbox.email, smtp, message)
