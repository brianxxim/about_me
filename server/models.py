from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Mailbox(db.Model):
    """
    help模型
    """
    __tablename__ = 'mailbox'

    id = db.Column(db.Integer, primary_key=True, doc='pk')
    name = db.Column(db.String, nullable=True, doc='姓名')
    phone = db.Column(db.String, nullable=True, doc='手机')
    email = db.Column(db.String, nullable=False, doc='邮箱')
    subject = db.Column(db.String, nullable=False, doc='主题')
    message = db.Column(db.Text, nullable=False, doc='内容')

