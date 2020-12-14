import settings
from settings import IP,headers
from tools.logger import GetLogger
logger=GetLogger().get_logger()
class ApiBuy:
    def __init__(self):
        logger.info('开始获取下订单接口的URL：')
        self.url=IP+'/mtx/index.php?s=/index/buy/add.html'
        logger.info('下订单接口的URL地址是{}'.format(self.url))
    def apiBuy(self,session):
        logger.info('开始获取下订单接口的data数据：')
        data={
            'goods_id': 1,
            'stock': 1,
            'buy_type': 'goods',
            'address_id': 1290,
            'payment_id': 1,
            'spec': '',
        }
        logger.info('开始获取下订单接口的data数据是：{}'.format(data))
        logger.info('开始发送下订单接口请求：')
        res_buy=session.post(self.url,data=data,headers=headers)
        logger.info('获取下订单接口的响应：{}'.format(res_buy.json()))
        settings.JUMP_URL=res_buy.json().get('data').get('jump_url')
        logger.info('下订单接口的响应的JUMP_URL是：{}'.format(settings.JUMP_URL))
        return  res_buy
