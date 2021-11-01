"""
业务层的封装，封装一些公共方法，比如公共api等
"""
import json

from feishu.api.base_api import BaseApi
from feishu.utils.logger import logger


class FeishuApi(BaseApi):
    app_id = "cli_a1f7b81aec39d00c"
    app_secret = "KWNxqOCiHEMdoUXxmcsuEeQTKCtehiSH"

    def feishu_requests(self, method, url , **kwargs):
        # 因为飞书的业务需求，所以需要在头信息塞入token
        # 本身有头信息， 在头信息内塞入认证
        if "headers" in kwargs:
            kwargs["headers"]["Authorization"] = f"Bearer {self.get_token()}"
        else:
            kwargs["headers"] = {"Authorization": f"Bearer {self.get_token()}"}

        r = self.base_requests(method = method, url = url, **kwargs)
        # 如果确定你的业务响应都是json，那么可以直接return r.json()
        # forrmat_json = json.dumps(r.json(), indent=2, ensure_ascii=False)
        return r.json()

    def get_token(self):
        token_url ="https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
        json_data = {
            "app_id": self.app_id,
            "app_secret": self.app_secret
        }
        r = self.base_requests(url = token_url, method="post", json = json_data)
        self.token = r.json()["tenant_access_token"]
        logger.debug(f"获取token的响应信息为{r.json()}")
        return self.token