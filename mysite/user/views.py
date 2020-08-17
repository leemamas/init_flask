# *_* coding : UTF-8 *_*
from . import user_blue
# from flask import current_app
# import logging
from flask import current_app
@user_blue.route('/')
def index():
    # logging.debug('debug msg')
    current_app.logger.debug('debug msg')
    return 'index'
