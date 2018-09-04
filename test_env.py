# coding:utf-8
from commons.log import get_logger
import os
import yaml
from requests import session
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

logger = get_logger(__name__)
conf_path = os.path.join(os.path.dirname(__file__), "environments")


class ResponseHandler(object):
    def __call__(self, resp, *args, **kwargs):
        logger.info('### Request start###')
        logger.info('Method:{0}, URL:{1}'.format(resp.request.method, resp.request.url))
        # logger.info('URL:{0}'.format(resp.request.url))
        logger.info('Header:{0}'.format(resp.request.headers))
        logger.info('Body:{0}'.format(resp.request.body))
        logger.info('### Response ###')
        logger.info('Status:{0}'.format(resp.status_code))
        logger.info('Header:{0}'.format(resp.headers))
        logger.info('Body:{0}'.format(resp.text))
        logger.info('### Request end###')


def create_session(conf_name="pre_product"):
    with open(os.path.join(conf_path, conf_name)) as f:
        conf = yaml.load(f)
    ss = session()
    # Update session from config
    for key in conf:
        setattr(ss, key, conf[key])
    # update header
    ss.headers.update(ss.default_header)
    ss.hooks = {'response': ResponseHandler()}
    return ss
