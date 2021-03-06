from feishu.api.calendar import Calendar


class TestCalendar:

    def setup_class(self):
        self.calendar = Calendar()

    def test_get(self):
        self.calendar.get("feishu.cn_Y5ytegaatFxDUBUYAVSnQg@group.calendar.feishu.cn")

    def test_create_success(self):
        r = self.calendar.create(summary="冰镇西瓜")
        calendar_id = r["data"]["calendar"]["calendar_id"]
        # 1. 通过别的业务接口完成测试
        # 2. 封装一些数据库操作，读取数据库完成断言
        get_res = self.calendar.get(calendar_id)
        # 业务逻辑的校验，确定日历已经创建成功
        assert get_res["code"] == 0

    def test_create(self):
        # 创建日历， 获取日历，断言日历是否创建成功
        r = self.calendar.create(summary="冰镇西瓜")
        # 单接口校验，查看响应值是否为设定的内容
        assert r["data"]["calendar"]["summary"] == "冰镇西瓜"


