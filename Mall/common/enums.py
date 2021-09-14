from enum import Enum
class AssertType(str, Enum):
    containsString = 'containsString'
    equalTo = 'equalTo'
    greaterThanOrEqualTo = 'greaterThanOrEqualTo'
    lessThanOrEqualTo = 'lessThanOrEqualTo'
    hasSize = 'hasSize'
    hasValue = 'hasValue'
    hasKey = 'hasKey'

class ContentType(Enum):
    JSON = 'application/json'
    DATA = 'multipart/form-data'
    FORM = 'application/x-www-form-urlencoded'

class Severity(str, Enum):
    BALOCKER = 'blocker'
    CRITICAL = 'critical'
    NORMAL = 'normal'
    MINOR = 'minor'
    TRIVIAL = 'trivial'

class Method:
    GET = 'get'
    POST = 'post'
    DELETE = 'delete'