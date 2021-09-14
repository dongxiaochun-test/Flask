class ResultCode:
    def __init__(self, code, message):
        self.__code = code
        self.__message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message):
        self.__message = message

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code):
        self.__code = code

    @staticmethod
    def SUCCESS():
        return ResultCode(200, '操作成功')

    @staticmethod
    def FAILED():
        return ResultCode(500, '操作失败')

    @staticmethod
    def VALIDATE_FILED():
        return ResultCode(404, '参数验证失败')

    @staticmethod
    def UNAUTHORIZED():
        return ResultCode(401, '未登录或token已过期')

    @staticmethod
    def FORBIDDEN():
        return ResultCode(403, '没有相关权限')

    @staticmethod
    def JSONDECODE_ERROR():
        return ResultCode(405, 'Json文件解析错误')