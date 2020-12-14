
from settings import IP,headers
from tools.logger import GetLogger
logger=GetLogger().get_logger()
class ApiLogin:
    def __init__(self):
        logger.info('开始获取登录接口的URL：')
        self.url=IP+'/mtx/index.php?s=/index/user/login.html'
        logger.info('登录接口的URL是{}'.format(self.url))

    def login(self,session,data):
        '''
        对登陆接口进行自动化测试
        data post,get 请求参数1、参数化 业务层验证 2、验证功能 直接写死
        '''
        logger.info('开始发送登录接口请求，参数是{}，header是{}'.format(data,headers))
        res_login=session.post(self.url,data=data,headers=headers)
        logger.info('获取响应值是{}'.format(res_login.json()))
        return res_login
    def loginsucess(self,session):

        '''
        与关联接口进行关联，发起登录成功的请求
        :return:
        '''
        logger.info('准备发起登录成功的请求')
        data={'accounts':'yaoyao','pwd':'yaoyao'}
        logger.info('登录成功的data数据是{}'.format(data))
        res_loginsucess=session.post(self.url,data=data,headers=headers)
        logger.info('登录成功的响应值是{}'.format(res_loginsucess.json()))
        return res_loginsucess