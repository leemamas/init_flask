# *_* coding : UTF-8 *_*
import redis

class Config(object):

    SECRET_KEY='sadqe1#@ms435?dsfwe'

    #数据库
    SQLALCHEMY_DATABASE_URI ='mysql://root:toor@127.0.0.1:3306/data_flask'
    SQLALCHEMY_TRACK_MODIFICATIONS =True


    #redis
    REDIS_HOST='192.168.102.128'
    REDIS_PORT=7000
    REDIS_PASSWORD='123456'

    #session
    SESSION_TYPE='redis'
    SESSION_REDIS=redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT,password=REDIS_PASSWORD)
    # 是否对发送到浏览器上session的cookie值进行加密，隐藏session_id
    SESSION_USE_SIGNER=True
    # 如果设置session的生命周期是否是会话期, 为True，则关闭浏览器session就失效
    #SESSION_PERMANENT = False
    #有效期，以秒为单位,86400为1天
    PERMANENT_SESSION_LIFETIME=86400


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass

config={
    'develop':DevelopmentConfig,
    'product':ProductionConfig
}