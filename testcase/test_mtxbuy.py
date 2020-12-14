import pytest
import  allure
import requests
from api.api_buy import ApiBuy
from api.api_loginmtx import ApiLogin
class TestBuy:
    def setup_class(self):
        self.session=requests.session()
        self.BuyObject=ApiBuy()
        ApiLogin().loginsucess(self.session)
    @allure.story('码同学商城下订单功能')
    @allure.title('码同学商城下单提交成供')
    @allure.severity('blocker')
    def test_buy(self):
        res_buy=self.BuyObject.apiBuy(self.session)
        assert  res_buy.json().get('msg') == '提交成功'