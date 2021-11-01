"""
和接口操作相关的封装， 不关心具体的业务
"""

import requests

from feishu.utils.logger import logger


class BaseApi:
    def base_requests(self, method, url, **kwargs):

        logger.debug(f"请求的参数为{method}, 请求url为{url}")
        r = requests.request(method, url, **kwargs)

        return r
