from typing import Text

from graduation.apiRunner.models import TStep, TRequest, RequestMethod


class RequestWithOptionalArgs:
    """
    填充请求可选参数
    """

    def __init__(self, step_context: TStep):
        self.__step_context = step_context

    def with_params(self, **params) -> 'RequestWithOptionalArgs':
        self.__step_context.request.params.update(params)
        return self

    def with_data(self, **data) -> 'RequestWithOptionalArgs':
        self.__step_context.request.data = data
        return self

    def with_json(self, **json) -> 'RequestWithOptionalArgs':
        self.__step_context.request.req_json = json
        return self

    def with_headers(self, **headers) -> 'RequestWithOptionalArgs':
        self.__step_context.request.params.update(headers)
        return self

    def with_cookies(self, **cookies) -> 'RequestWithOptionalArgs':
        self.__step_context.request.cookies.update(cookies)
        return self

    def with_files(self, **files) -> 'RequestWithOptionalArgs':
        self.__step_context.request.files.update(files)
        return self

    def set_timeout(self, timeout: float) -> 'RequestWithOptionalArgs':
        self.__step_context.request.timeout = timeout
        return self

    def set_allow_redirects(self, allow_redirects: bool) -> 'RequestWithOptionalArgs':
        self.__step_context.request.allow_redirects = allow_redirects
        return self

    def set_verify(self, verify: bool) -> 'RequestWithOptionalArgs':
        self.__step_context.request.verify = verify
        return self

    def perform(self) -> TStep:
        '''
        填充完数据后，需要然后一个TStep对象
        '''
        return self.__step_context


# 创建RunRequest对象时，在RunRequest类初始化函数中创建一个TStep对象，通过调用get等方法创建一个TRequest对象
class RunRequest:
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

    def patch(self, url: Text) -> RequestWithOptionalArgs:
        self.__step_context.request = TRequest(method=RequestMethod.PATCH, url=url)
        return RequestWithOptionalArgs(self.__step_context)
