import requests
from common.resultcode import ResultCode
class CommonResult:

    def __init__(self, code, message, data=None):
        self.__code = code
        self.__message = message
        self.__data = data

    @property
    def code(self):
        return self.__code

    @property
    def message(self):
        return self.__message

    @property
    def data(self):
        return self.__data

    @staticmethod
    def success(data, code=None, message=None):
        """
        返回请求成功对应的数据信息
        :param data: 需要封装的数据对象
        :param message: 提示信息
        :return: CommonResult 对象
        """
        result = ResultCode.SUCCESS() # 获取成功的状态码及对应提示信息
        if message:
            result.message = message
        if code:
            result.code = code
        return CommonResult(result.code,result.message,data)

    @staticmethod
    def failed(code=None, message=None):
        result = ResultCode.FAILED()  # 获取成功的状态码及对应提示信息
        if message:
            result.message = message
        if code:
            result.code = code
        return CommonResult(result.code,result.message)

    @staticmethod
    def validateFailed(message=None):
        result = ResultCode.VALIDATE_FILED()
        if message:
            result.message = message
        return CommonResult(result.code, result.message)

    @staticmethod
    def unauthorized(data=None):
        result = ResultCode.UNAUTHORIZED()
        return CommonResult(result.code, result.message, data)

    @staticmethod
    def foribdden(data=None):
        result = ResultCode.FORBIDDEN()
        return CommonResult(result.code, result.message, data)

    @staticmethod
    def jsonDecodeError(data=None):
        result = ResultCode.JSONDECODE_ERROR()
        return CommonResult(result.code, result.message, data)

if __name__ == '__main__':
    res = requests.get('https://petstore.swagger.io/v2/pet/99')

    CommonResult.success(res.json(), res.status_code)



