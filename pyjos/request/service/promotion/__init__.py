from . import app, batch
from ... import BaseRequest, parameter


class getcode(BaseRequest):
    """自定义链接转换接口"""
    def __init__(self, **kwargs):
        super(getcode, self).__init__(**kwargs)

    @property
    def api_method_name(self):
        return 'jingdong.service.promotion.getcode'

    promotionType = parameter(attr='promotionType', default=1, validators=[], doc='推广类型 1：商品推广 2:店铺推广 3 活动推广 4 频道页推广 5 搜索推广 0 其他'),

    materialId = parameter('materialId', validators=[], doc='')


class appReport(object):
    pass


class goodsInfo(object):
    pass
