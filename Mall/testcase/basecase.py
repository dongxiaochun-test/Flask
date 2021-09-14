from common.enums import Method, AssertType
from report.reporter import report
from log.log import logger

class BaseCase:
    def execute(self, client, data):
        """
        执行通用测试用例
        :param client:
        :param data:
        :return:
        """
        headers = data.get('desc').get('headers')
        method = data.get('desc').get('method')
        if method.lower() == Method.GET:
            response = client.get(url=data.get('desc').get('url'), headers=headers)
        elif method.lower() == Method.POST:
            response = client.post(url=data.get('desc').get('url'), data=data.get('data'), headers=headers)

        # 动态获取断言信息，遍历方式
        self.assertCase(response, data.get('asserts'))
        # # 输出测试报告
        report(data=data, result=response)

    def assertCase(self, response, asserts):
        '''
        对所有数据做断言
        :param response: 实际结果
        :param asserts: 期望结果
        :return:
        '''
        # 循环遍历断言类型
        for key in asserts.keys():
            # 获取待验证的值
            checkedValue = asserts.get(key)
            if key == AssertType.equalTo:
                # 循环遍历要断言的值
                for subkey in checkedValue.keys():
                    # 当subkey是多级节点，进行循环取出实际返回的节点值
                    data = self.fetchData(subkey,response)
                    assert checkedValue.get(subkey) == data
                    # subkey='data.haha.xixi'
                    # items = subkey.split('.')   # items[0]--data items[1]--haha items[2]--xixi
                    # ss = response.get(items[0]) # ss--{'huice':'www.huicewang.com','auto':'testing','haha':{'xixi':900}}
                    # ss.get(items[1]) # 'haha':{'xixi':900}
                    # ss = ss.get(items[2]) # 900

            elif key == AssertType.containsString:
                for subkey in checkedValue.keys():
                    data = self.fetchData(subkey,response)
                    assert checkedValue.get(subkey) in data
            elif key == AssertType.greaterThanOrEqualTo:
                for subkey in checkedValue.keys():
                    data = self.fetchData(subkey,response)
                    assert checkedValue.get(subkey) <= data
            elif key == AssertType.lessThanOrEqualTo:
                for subkey in checkedValue.keys():
                    data = self.fetchData(subkey,response)
                    assert checkedValue.get(subkey) >= data
            elif key == AssertType.hasSize:
                for subkey in checkedValue.keys():
                    data = self.fetchData(subkey,response)
                    assert checkedValue.get(subkey) == len(data)
            else:
                logger.error('断言类型不存在，出错')
                
    def fetchData(self, key, response):
        '''
        根据key的值取出json中相应的数据
        :param key:
        :param response:
        :return:
        '''
        items = key.split('.')
        if len(items) > 1:
            for item in items:
                response = response.get(item)
        else:
            response = response.get(key)
        return response


if __name__ == '__main__':
    # 模拟请求返回的实际结果
    response = {
          "code": 200,
          "message": "获取验证码成功",
          "data": {'huice':'www.huicewang.com','auto':'testing','haha':{'xixi':900}},
          "huice":300
    }

    # 测试用例的断言部分
    asserts = {
        AssertType.equalTo:{
            'code':200,
            'data.haha.xixi':900,
            'data.huice':'www.huicewang.com'
        },
        AssertType.containsString:{
            'message': '成功',
            'data.auto':'test'
        },
        AssertType.greaterThanOrEqualTo:{# 期望实际结果大于等于150
            'huice':150
        },
        AssertType.hasSize:{
            'data':3
        }
    }
    baseCase = BaseCase()
    baseCase.assertCase(response,asserts)

    # 验证code是否等于200，message中是否包含 成功 两个字, data中的值是否等于 408658



# 1、定义常见的断言类型（条件）

# 用例生成（数据）--自动化
# 用例执行--自动化
#     pytest
# 结果验证--自动化
#     断言设计