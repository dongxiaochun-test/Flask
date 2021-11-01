"""
飞书的日历管理模块
"""
from feishu.api.feishu_api import FeishuApi
from feishu.utils.logger import logger


class Calendar(FeishuApi):
    """
    接口的具体实现内容
    """

    # 接口用例逻辑和接口本身逻辑保持一致
    def create(self, summary="hogwarts_ad",
               description="使用开放接口创建日历hogwarts_ad",
               permissions="public",
               color=-1,
               summary_alias="hogwarts_Adddddds"):
        url = "https://open.feishu.cn/open-apis/calendar/v4/calendars"
        method = "POST"

        json_data = {
                "summary": summary,
                "description": description,
                "permissions": permissions,
                "color": color,
                "summary_alias": summary_alias
            }
        r = self.feishu_requests(url= url, method=method, json = json_data)
        logger.info(f"创建接口的响应值信息为{r}")
        return r



    def delete(self):
        pass

    def get(self, calendar_id):
        url = f"https://open.feishu.cn/open-apis/calendar/v4/calendars/{calendar_id}"
        r = self.feishu_requests(url = url, method= "get")
        logger.info(f"获取接口的响应值信息为{r}")
        return r

    def get_list(self):
        pass

    def update(self):
        pass

    def search(self):
        pass
