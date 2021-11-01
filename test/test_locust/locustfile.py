from locust import HttpUser, task
import queue

import loader

# 全局参数化，适合类似于注册业务
q = queue.Queue()
csv_list = loader.load_csv_file('./data/user.csv')
for item in csv_list:
    q.put(item)



class FecMallUser(HttpUser):
    host = 'http://appserver.huice.com'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.q = queue.Queue()

    # def on_start(self):
    #     csv_list = loader.load_csv_file('./data/user.csv')
    #     for item in csv_list:
    #         self.q.put(item)

    # wait_time = constant_throughput(3)
    # @task(1)
    # def open_index(self):
    #     headers = {'accept': 'application/json'}
    #     with self.client.get('/cms/home/index?page=3&total=200',
    #                          catch_response=True,
    #                          name='首页',
    #                          headers=headers) as response:
    #         if response.status_code != 200:
    #             response.failure('失败了')
    #     params = {'page': 3, 'total': 200}
    #
    #     with self.client.get('/cms/home/index',
    #                          catch_response=True,
    #                          params=params,
    #                          name='首页',
    #                          headers=headers) as response:
    #         if response.status_code != 200:
    #             response.failure('失败了')

    @task
    def login(self):
        item = q.get()
        data = {'email': item.get('email'), 'password': item.get('password')}
        response = self.client.post(url='/customer/login/account', data=data)
        d = response.json()
        # self.q.put(item) # 确保数据循环使用
