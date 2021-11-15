from enum import Enum
from typing import Text, Dict, Union, Any, List
from pydantic import BaseModel


class RequestMethod(Text, Enum):
    """
    封装常见的请求方法
    """
    GET = 'GET'
    POST = 'POST'
    DELETE = 'DELETE'
    PUT = 'PUT'
    PATCH = 'PATCH'
    OPTIONS = 'OPTIONS'
    HEAD = 'HEAD'


class TRequest(BaseModel):
    """
    封装请求数据
    """

    method: RequestMethod
    url: Text
    params: Dict[Text, Text] = {}
    data: Union[Text, Dict[Text, Any]] = None
    req_json: Union[Dict, List, Text] = None
    headers: Dict[Text, Text] = {}
    cookies: Dict[Text, Text] = {}
    files: Dict = {}
    timeout: float = 120
    allow_redirects: bool = True
    verify: bool = False


class TStep(BaseModel):
    """
    封装测试步骤信息
    """
    # 测试步骤名称
    name: Text
    # 请求对象（存储需要请求的参数信息）
    request: Union[TRequest, None] = None
    # 存储需要导出的返回数据信息
    extract: Dict[Text, Any] = {}
    # 存储当前步骤的断言信息
    validators: List[Dict] = None
