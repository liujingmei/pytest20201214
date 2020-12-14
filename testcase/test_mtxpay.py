import pytest
import allure
import requests
from api.api_pay import ApiPay
from api.api_buy import ApiBuy
from api.api_loginmtx import ApiLogin
class TestPay:
    def setup_class(self):
        self.session=requests.session()
        ApiLogin().loginsucess(self.session)
        ApiBuy().apiBuy(self.session)
        self.payobject = ApiPay()
    @allure.feature('码同学商城接口测试')
    @allure.story('码同学商城支付接口测试')
    @allure.title('支付成功测试')
    @allure.severity('blocker')
    def test_pay(self):
        res_pay=self.payobject.apipay(self.session)
        assert '支付成功' in res_pay.text