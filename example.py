# coding: utf-8
"""一个比较简陋的example， TODO: 创建业务参数的request"""
import json
import os

from pyjos.client import JdClient
from pyjos import request as jingdong

PROJECT_DIR = os.path.dirname(__file__)

try:
    # secrets.json example
    # {
    #   "app_key": "26EAC2509056EB38FB623D9A49296D2C",
    #   "app_secret": "1abdc5a97ecb4594ab7b772296bcfbbd",
    #   "access_token": "1f1d3048-220a-484d-ad93-f3808d9aacc1"
    # }
    # https://jos.jd.com/doc/channel.htm?id=152
    # TODO: Add OAuth2 request to get the access_token
    #
    # config.json example
    # config.json holds a particular API call's parameters.
    # {
    #   "promotionType": 1,
    #   "materialId": "",
    #   "unionId": "",
    # }
    # https://jos.jd.com/api/detail.htm?apiName=jingdong.service.promotion.getcode&id=1648
    with open(os.path.join(PROJECT_DIR, 'secrets.json')) as secrets,\
            open(os.path.join(PROJECT_DIR, 'config.json')) as config:
        SECRETS = json.load(secrets)
        CONFIG = json.load(config)
except IOError:
    raise


def main():
    """Main function"""
    example_request = jingdong.service.promotion.getcode(**CONFIG)

    client = JdClient()
    client.app_key = SECRETS['app_key']
    client.app_secret = SECRETS['app_secret']
    print(client.execute(example_request, SECRETS['access_token']))

if __name__ == '__main__':
    main()
