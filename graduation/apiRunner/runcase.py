from typing import Text

from graduation.apiRunner.models import TStep, TRequest, RequestMethod
from graduation.apiRunner.testcase import RequestWithOptionalArgs


class RunRequest:
    """
    创建请求步骤及请求对象
    """
    def __init__(self, name: Text):
        # 创建一个TStep对象
        self.__step_context = TStep(name=name)

    def get(self, url: Text) -> RequestWithOptionalArgs:
        self.__step_context.request = TRequest(method=RequestMethod.GET, url=url)
        return RequestWithOptionalArgs(self.__step_context)

    def post(self, url: Text) -> RequestWithOptionalArgs:
        self.__step_context.request = TRequest(method=RequestMethod.POST, url=url)
        return RequestWithOptionalArgs(self.__step_context)

    def put(self, url: Text) -> RequestWithOptionalArgs:
        self.__step_context.request = TRequest(method=RequestMethod.PUT, url=url)
        return RequestWithOptionalArgs(self.__step_context)

    def head(self, url: Text) -> RequestWithOptionalArgs:
        self.__step_context.request = TRequest(method=RequestMethod.HEAD, url=url)
        return RequestWithOptionalArgs(self.__step_context)

    def delete(self, url: Text) -> RequestWithOptionalArgs:
        self.__step_context.request = TRequest(method=RequestMethod.DELETE, url=url)
        return RequestWithOptionalArgs(self.__step_context)

    def options(self, url: Text) -> RequestWithOptionalArgs:
        self.__step_context.request = TRequest(method=RequestMethod.OPTIONS, url=url)
        return RequestWithOptionalArgs(self.__step_context)