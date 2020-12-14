import settings
from tools.logger import GetLogger
logger=GetLogger().get_logger()
class ApiPay:
    def __init__(self):
        logger.info('即将开始获取支付订单接口的url')
        self.url=settings.JUMP_URL
        logger.info('支付订单接口的url是{}'.format(self.url))
    def apipay(self,session):
        logger.info('开始发送支付订单接口的请求')
        res_pay=session.get(self.url,allow_redirects=False)
        logger.info('获取到支付订单的接口响应是{}'.format(res_pay.headers))
        logger.info('开始获取支付订单接口的响应头信息中的location{}，并对其发起请求'.format(res_pay.headers['location']))
        res_payheader=session.get(res_pay.headers['location'])
        logger.info('获取支付订单接口location请求的响应：{}'.format(res_payheader.text))
        return res_payheader
