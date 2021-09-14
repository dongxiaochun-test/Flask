import pytest
from request.httpclient import HttpClient
import os
from config.config import Config
# 组件库
@pytest.fixture()
def client():
    c = HttpClient()
    yield c # 返回client，同时暂停后面代码的运行
    os.popen('allure generate ' + Config().resultpath + ' -o '+ Config().reportpath)
    c.close()

