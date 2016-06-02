# coding: utf-8
from datetime import datetime
import json
import hashlib

import requests
import six


def force_str(text):
    """Force convert a text encoding in utf-8 to str type in both 2 & 3"""
    if six.PY3:
        return str(text, encoding='utf-8')
    else:
        return str(text)


class JdClient(object):
    server_url = 'https://api.jd.com/routerjson'
    connect_timeout = 0
    read_timeout = 0
    app_key = ''
    app_secret = ''
    version = '2.0'
    format = 'json'
    json_param_key = '360buy_param_json'

    def __init__(self):
        self.timeout = (self.connect_timeout, self.read_timeout)

    def generate_sign(self, params):
        string_to_be_signed = self.app_secret
        for k, v in sorted(params.items()):
            print(k, v)
            if not v.startswith('@'):
                string_to_be_signed += '{}{}'.format(k, v)
        string_to_be_signed += self.app_secret
        signed_string = six.b(string_to_be_signed)
        return hashlib.md5(signed_string).hexdigest().upper()

    def execute(self, request, access_token=None):
        # 组装系统参数
        sys_params = {
            'app_key': self.app_key,
            'v': self.version,
            'method': request.get_api_method_name(),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }
        if access_token is not None:
            sys_params['access_token'] = access_token

        # 获取业务参数
        api_params = request.get_api_params()
        sys_params[self.json_param_key] = api_params

        # 签名
        sys_params['sign'] = self.generate_sign(sys_params)
        # 发起请求
        response = requests.get(url=self.server_url, params=sys_params)
        response.raise_for_status()

        if self.format == 'json':
            response_object = json.loads(force_str(response.content))

        elif self.format == 'xml':
            raise NotImplementedError('At the moment I write this, JD haven\'t'
                                      'support the xml format')
        else:
            raise KeyError('HTTP response not well formed')
        return response_object
