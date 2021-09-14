from mimesis import Person,Datetime,locales
from mimesis.enums import Gender
from mimesis.schema import Field,Schema
from common.enums import Method,Severity,AssertType,ContentType
from common import datagenerator

class AuthCodeCaseData:

    @classmethod
    def success_case(cls, iterartion=1):
        '''
        构造合法的电话号码数据
        :param iterartion: 数据的条数
        :return: 整个数据及验证信息
        '''
        schmea = Schema(schema=lambda: {
            'desc': {  # 用例描述信息
                'url': 'http://121.37.169.128:8201/mall-member/sso/getAuthCode?telephone=' + datagenerator.telephone(),
                'method': Method.GET,
                'module': '会员管理',
                'title': '获取验证码',
                'severity': Severity.CRITICAL  # blocker,critical,normal,minor,trivial
            },
            'data': {  # 测试数据
            },
            'headers':{
            },
            'asserts': {  # 断言
                AssertType.equalTo:{
                    'code':200,
                },
                AssertType.containsString:{
                    'message':'成功'
                }

               }})
        return schmea.create(iterations=iterartion)

class RegisterCaseData:

    @classmethod
    def success_case(cls, iterartion=1):
        '''
        会员注册
        :param iterartion: 数据的条数
        :return: 会员注册信息
        '''
        p = Person()
        schmea = Schema(schema=lambda: {
            'desc': {  # 用例描述信息
                'url': 'http://121.37.169.128:8201/mall-member/sso/register',
                'method': Method.POST,
                'module': '会员管理',
                'title': '会员注册-数据合法',
                'severity': Severity.CRITICAL  # blocker,critical,normal,minor,trivial
            },
            'data': {  # 测试数据
                'authCode':'',
                'password': '123456',
                'telephone': '',
                'username': p.username('Ud')
            },
            'headers':{
                'Content-Type':ContentType.FORM
            },
            'asserts': {  # 断言
                AssertType.equalTo:{
                    'code':200,
                },
                AssertType.containsString:{
                    'message':'成功'
                }

               }})
        return schmea.create(iterations=iterartion)

    @classmethod
    def success_json_case(cls):
        pass

    @classmethod
    def success_yaml_case(cls):
        pass

    @classmethod
    def success_excel_case(cls):
        pass

    @classmethod
    def failed_case(cls, iterartion=1):
        '''
        会员注册
        :param iterartion: 数据的条数
        :return: 会员注册信息
        '''
        p = Person()
        schmea = Schema(schema=lambda: {
            'desc': {  # 用例描述信息
                'url': 'http://121.37.169.128:8201/mall-member/sso/register',
                'method': Method.POST,
                'module': '会员管理',
                'title': '会员注册-数据不合法',
                'severity': Severity.CRITICAL  # blocker,critical,normal,minor,trivial
            },
            'data': {  # 非法测试数据
                'authCode':'661282',
                'password': '123456',
                'telephone': '13401182883',
                'username': p.username('Ud'),
            },
            'headers':{
                'Content-Type': ContentType.FORM
            },
            'asserts':
                {  # 断言
                    AssertType.equalTo: {
                        'status': 500,
                    },
                    AssertType.containsString: {
                        'error': 'Error'
                    }

                }})
        return schmea.create(iterations=iterartion)

# 测试代码
if __name__ == '__main__':
    data = AuthCodeCaseData.success_case(iterartion=1)
    print(data[0].get('data').get('telephone'))