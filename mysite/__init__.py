# *_* coding : UTF-8 *_*

from flask import Flask
from settings import config
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_session import Session
from flask_wtf import CSRFProtect
import logging
from logging.handlers import RotatingFileHandler

# 数据库
db = SQLAlchemy()

# redis
redis_store = None

csrf=CSRFProtect()

# 设置日志的的记录等级
logging.basicConfig(level=logging.DEBUG)
# 创建日志记录器，设置日志的保存路径和每个日志的大小和日志的总大小
file_log_handler = RotatingFileHandler("mysite/logs/log", maxBytes=1024*1024*100,backupCount=100)
# 创建日志记录格式，日志等级，输出日志的文件名 行数 日志信息
formatter = logging.Formatter("%(levelname)s %(filename)s: %(lineno)d %(message)s")
# 为日志记录器设置记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flaks app使用的）加载日志记录器
logging.getLogger().addHandler(file_log_handler)

def create_app(name):
    app = Flask(__name__)

    config_cls = config.get(name)
    app.config.from_object(config_cls)

    # 初始化db
    db.init_app(app)

    # 初始化 redis工具
    global redis_store
    redis_store = redis.StrictRedis(host=config_cls.REDIS_HOST, port=config_cls.REDIS_PORT,password=config_cls.REDIS_PASSWORD)

    Session(app)

    # crsf防护
    csrf.init_app(app)

    # 注册蓝图
    from mysite import user
    app.register_blueprint(user.user_blue)

    return app
