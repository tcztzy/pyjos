# coding: utf-8
"""一个比较简陋的example， TODO: 创建业务参数的request"""
import json
from pathlib import Path

from pyjos.client import JdClient

PROJECT_DIR = Path(__file__).resolve().parent

try:
    # 你懂的
    with PROJECT_DIR.joinpath('', 'secrets.json').open() as handle:
        SECRETS = json.load(handle)
    # 业务参数在此
    with PROJECT_DIR.joinpath('', 'config.json').open() as handle:
        CONFIG = json.load(handle)
except IOError:
    raise


class ExampleRequest(object):
    pass

example_request = ExampleRequest()

for k, v in CONFIG.items():
    setattr(example_request, k, v)

example_request.get_api_method_name = lambda: 'jingdong.service.promotion.getcode'

example_request.get_api_params = lambda: str(CONFIG)

client = JdClient()
client.app_key = SECRETS['app_key']
client.app_secret = SECRETS['app_secret']
print(client.execute(example_request, SECRETS['access_token']))
