from testcase.basecase import BaseCase
from testcase.mall_member.member_controller import RegisterCaseData
from common.business import getAuthCode
from common import datagenerator
import pytest
class TestRegister(BaseCase):
    # 定义很多接口--请求和响应
    # 接口进行整合+断言---》用例（一个或者多个接口组成，同时再加上断言）
    # 例如：一个用例包含5个接口 执行逻辑：接口1--》接口2--》接口3--》接口4--》接口5+断言

    # 参数化驱动
    @pytest.mark.register
    @pytest.mark.parametrize("data", RegisterCaseData.success_case(1))
    def test_register_success(self, client, data):
        # 1、生成一个电话号码：13401182883
        # 2、根据这个电话号码获取验证码：99999

        # 需要将1、2两步数据传给注册接口

        # 定义一个data字典,
        # 开始注册 data传给注册接口

        # 电话号码同一个
        telephone = datagenerator.telephone()   # 获取一个手机号

        # 获取验证码接口返回数据
        authcode = getAuthCode(telephone)

        data.get('data')['authCode'] = authcode
        data.get('data')['telephone'] = telephone

        self.execute(client, data)

    @pytest.mark.register
    @pytest.mark.parametrize("data", RegisterCaseData.failed_case(1))
    def test_register_failed(self, client, data):
        # 电话号码不是同一个
        telephone = datagenerator.telephone()
        authcode = getAuthCode(telephone)
        data['authCode'] = authcode
        data['telephone'] = datagenerator.telephone()

        self.execute(client, data)

if __name__ == '__main__':
    pytest.main(['-s', '-v', '--clean-alluredir', r'--alluredir=D:\workspace\huice21\MallAPITesting\venv\allure-results'])
