from enum import Enum
from typing import Text, Dict, Union, Any, List
from pydantic import BaseModel


class RequestMethod(Text, Enum):
    GET = 'GET'
    POST = 'POST'
    DELETE = 'DELETE'
    PUT = 'PUT'
    PATCH = 'PATCH'
    OPTIONS = 'OPTIONS'
    HEAD = 'HEAD'


class TRequest(BaseModel):
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
    name: Text
    request: Union[TRequest, None] = None
    extract: Dict[Text, Any] = {}
    validators: List[Dict]
