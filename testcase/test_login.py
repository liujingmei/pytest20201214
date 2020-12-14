import pytest
import allure
import requests
from api.api_loginmtx import ApiLogin
from tools.readData import ReadData
#yaml文件是列表套字典的格式
test_login=[]
data_li=ReadData().get_yaml('login_data','test_login')
class TestLogin:
    def setup_class(self):
        self.session=requests.session()
        #创建登录接口实例化对象
        self.loginobject=ApiLogin()
    @pytest.mark.parametrize('dic',data_li)
    @allure.feature('码同学商城功能测试')
    @allure.story('码同学商城登录功能测试')
    @allure.title('码同学商城登录测试')
    def test_login(self,dic):
        data={'accounts':dic['accounts'],'pwd':dic['pwd']}
        res=self.loginobject.login(self.session,data).json()
        assert res['msg'] == dic['exp']