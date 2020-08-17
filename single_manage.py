from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_session import Session
from flask_wtf import CSRFProtect

app = Flask(__name__)


class Config(object):
    DEBUG=True

    SECRET_KEY='sadqe1#@ms435?dsfwe'

    #数据库
    SQLALCHMEY_DATABASE_URL='mysql://root:torr@127.0.0.1:3306/data_flask?charset=utf8'
    SQLALCHMEY_TRACK_MODIFICATIONS=True

    #redis
    REDIS_HOST='127.0.0.1'
    REDIS_PORT=6379

    #session
    SESSION_TYPE='redis'
    SESSION_REDIS=redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
    # 是否对发送到浏览器上session的cookie值进行加密，隐藏session_id
    SESSION_USE_SIGNER=True
    # 如果设置session的生命周期是否是会话期, 为True，则关闭浏览器session就失效
    #SESSION_PERMANENT = False
    #有效期，以秒为单位,86400为1天
    PERMANENT_SESSION_LIFETIME=86400

app.config.from_object(Config)

db=SQLAlchemy(app)

redis_store=redis.StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)

Session(app)

#crsf防护
CSRFProtect(app)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
