# 封装get、put、delete、post
# 代码封装方式：1、直接在模块封装；2、在类中封装
import requests
import json
from log.log import logger
from common.commonresult import CommonResult
from requests_toolbelt import MultipartEncoder
from json import JSONDecodeError
import random
from common.enums import ContentType

class HttpClient:
    """
    完成客户端请求
    """
    def __init__(self, session = None):
        if session == None:
            self.__session = requests.session()
        else:
            self.__session = session

    def get(self, url, params=None, headers=None, cookies=None, timeout=6):
        response = self.__session.get(url=url, params=params, headers=headers, cookies=cookies, timeout=timeout)
        if response.status_code == 301:
            response = __session.get(url=response.headers.get('location'), params=params, headers=headers, cookies=cookies, timeout=timeout)
        try:
            # 将服务器返回的json数据转换成字典
            data = response.json()
        except JSONDecodeError as e:
            # 错误信息记录到日志文件
            logger.error(e.msg)
            # 数据格式转换出错，返回出错的数据信息
            return CommonResult.jsonDecodeError(response.text)
        return data
        # return CommonResult.success(code=data.get('code'),message=data.get('message'),data=data.get('data'))

    def post(self, url, data=None, headers=None, files=None, cookies=None, timeout=8):
        headers = {} if headers is None else headers
        if headers.get('Content-Type') == ContentType.JSON:   #请求json格式数据
            if isinstance(data, dict):
                response = self.__session.post(url=url, json=data, headers=headers, cookies=cookies, timeout=timeout)
            else:
                response = self.__session.post(url=url, data=data, headers=headers, cookies=cookies, timeout=timeout)
        elif headers.get('Content-Type') == ContentType.DATA: # 上传文件
            files.replace('\\','/')
            filename = files.split('/')[-1]

            # 合并data表单和file信息
            d = data.copy()
            d.update({'file':(filename,open(files,'rb'))})
            # print(d)
            enc = MultipartEncoder(
                # fields = {'file':(filename,open(files,'rb'))},
                fields = d,
                boundary = '----' + str(random.randint(1e28,1e29 - 1)) # 可选
            )
            headers['Content-Type'] = enc.content_type
            response = self.__session.post(url=url, data=enc, headers=headers, cookies=cookies, timeout=timeout)

        else: # 默认提交表单格式数据
            response = self.__session.post(url=url, data=data, headers=headers, cookies=cookies, timeout=timeout)

        try:
            # 将服务器返回的json数据转换成字典
            data = response.json()
        except JSONDecodeError as e:
            # 错误信息记录到日志文件
            logger.error(e.msg)
            # 数据格式转换出错，返回出错的数据信息
            return CommonResult.jsonDecodeError(response.text)

        return data
        # 返回数据中必须包含code、message、data信息
        # return CommonResult.success(code=data.get('code'),message=data.get('message'),data=data.get('data'))

    def put(self, url, data=None, headers=None, files=None, cookies=None, timeout=8):
        headers = {} if headers is None else headers
        if headers['Content-Type'] == ContentType.JSON:   #请求json格式数据
            response = self.__session.put(url=url, data=data, headers=headers, cookies=cookies, timeout=timeout)
        try:
            # 将服务器返回的json数据转换成字典
            data = response.json()
        except JSONDecodeError as e:
            # 错误信息记录到日志文件
            logger.error(e.msg)
            # 数据格式转换出错，返回出错的数据信息
            return CommonResult.jsonDecodeError(response.text)
        return data
        # return CommonResult.success(code=data.get('code'),message=data.get('message'),data=data.get('data'))

    def delete(self, url, params, headers, cookies=None, timeout=8):
        response = self.__session.delete(url=url, params=params, headers=headers, cookies=cookies, timeout=timeout)

        try:
            # 将服务器返回的json数据转换成字典
            data = response.json()
        except JSONDecodeError as e:
            # 错误信息记录到日志文件
            logger.error(e.msg)
            # 数据格式转换出错，返回出错的数据信息
            return CommonResult.jsonDecodeError(response.text)
        return data
        # return CommonResult.success(code=data.get('code'),message=data.get('message'),data=data.get('data'))

    def close(self):
        self.__session.close()
if __name__ == '__main__':
    client1 = HttpClient()
    # client调用的所有方法，它们是共享session的
    client2 = HttpClient()
    
    headers = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJhZG1pbiIsInNjb3BlIjpbImFsbCJdLCJpZCI6MywiZXhwIjoxNjI2MTgxOTgxLCJhdXRob3JpdGllcyI6WyI1X-i2hee6p-euoeeQhuWRmCJdLCJqdGkiOiI4YjU0MDQ4Mi04NjNkLTQ0ZjctYWQwNi0xZDA1MjdiNTQzYzkiLCJjbGllbnRfaWQiOiJhZG1pbi1hcHAifQ.Rwo48uyb_210t7rRXuL83_tXrSzTV3wqRyBds0cgCiMOqI5Yvv6u3Wt3G66IpfE0DdSfb5BqbL_DFT3_ZCxHGOqBNgwdztBCo8F8oOMc95-aeqGStAWUS-RKH1jqq-W2K6cslTpFcS9WfMBgLQ4XsmyYw44_1CKvaSD6OlDs-6U'}
    res = client.get(url='http://121.37.169.128:8201/mall-admin/aliyun/oss/policy', headers=headers)
    print(res.data.get('data').get('policy'))









    # res = client.get(url='https://editor.swagger.io/')
    # print(res.code)
    # print(res.message)
    # print(res.data)

    # s = 'c:\\aa\\bb\\a.jpg'
    # res = client.post(url='https://petstore.swagger.io/v2/pet/2/uploadImage',headers={}, contenttype='data', files=r'C:/Users/Administrator/Pictures/jiagou.png')
    # print(res.code)
    # print(res.message)
    # print(res.data)
    # dataD = {
    #     "id": 0,
    #     "category": {
    #         "id": 0,
    #         "name": "hhhhh22"
    #     },
    #     "name": "cccccccccccc222",
    #     "photoUrls": [
    #         "string"
    #     ],
    #     "tags": [
    #         {
    #             "id": 0,
    #             "name": "string"
    #         }
    #     ],
    #     "status": "available"
    # }
    # client = HttpClient()
    # # headers = {'Content-Type': 'application/json'}
    # # dataD--Python字典
    # response = client.post(url='https://petstore.swagger.io/v2/pet', data=dataD)
    # print(response.text)


    # user = {'username': 'admin', 'password': 'admin'}
    #
    # client = HttpClient()
    # response = client.post(url='http://flash-admin.enilu.cn/prod-api/account/login', data=user)
    # token = response.get('data').get('data').get('token')
    # headers = {'Authorization': token}
    #
    # url = 'http://flash-admin.enilu.cn/prod-api/dept?simplename=xixi&fullname=xixixixx&num=2&pid=1'
    # response = client.post(url=url,headers=headers)
    #
    # print(response)