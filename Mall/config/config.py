# from 父 import 子
import configparser
import json
import threading
# 属性尽量不要直接获取，而是通过方法进行封装
# 属性信息尽量是私有的
# 基本目标：实现单例模式

class Config:
    # 类成员，引用方式是：类名.类成员名称，例如：Config.__configfile
    __falg = False
    __configfile = r'D:\workspace\huice21\MallAPITesting\venv\config\config.ini'
    # __haha = None

    # 定义一把锁
    __instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        """
        构造函数
        :param args:
        :param kwargs:
        """
        # if cls.__haha is None:
        #     print('哈哈')
        #     cls.__haha = super().__new__(cls)
        # return cls.__haha

        if not hasattr(cls, '_instance'):
            # 获取锁
            cls.__instance_lock.acquire()
            if not hasattr(cls, '_instance'):
                # 创建一个对象
                cls._instance = super().__new__(cls)
            cls.__instance_lock.release()

        return cls._instance

    def __init__(self):
        """
        初始化函数，所有实例变量的定义及初始化都在这里完成
        """
        if Config.__falg:
            return

        config = configparser.ConfigParser()
        config.read(Config.__configfile)
        self.__host = config.get('database', 'host')
        self.__dbname = config.get('database', 'dbname')
        self.__username = config.get('database', 'username')
        self.__password = config.get('database', 'password')
        self.__port = config.get('database', 'port')
        self.__logpath = config.get('log', 'path')
        self.__resultpath = config.get('report', 'result_path')
        self.__reportpath = config.get('report', 'report_path')
        Config.__falg = True

    @property
    def host(self):
        return self.__host

    @property
    def dbname(self):
        return self.__dbname

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def port(self):
        return int(self.__port)

    @property
    def logpath(self):
        return self.__logpath

    @property
    def reportpath(self):
        return self.__reportpath

    @property
    def resultpath(self):
        return self.__resultpath

#
# def readIni():
#     config = configparser.ConfigParser()
#     # config.read('../config/config.ini')
#     config.read(r'D:\workspace\21\APITesting\venv\config\config.ini')
#     host = config.get('database', 'host')
#     path = config.get('log', 'path')
#     print(host)
#     print(path)
#
# def readJson():
#     j = '{"username":"huice","password":"123456"}'  # 符合json规范的普通字符串
#     d = json.loads(j)   # 将json字符串转换成Python的字典
#     # fd = json.load()  # 将json文件转换成Python的字典
#
#     print(d)
#     d = {'username':'huice','password':'123456'}    # python字典
#     j = json.dumps(d)
#
#     print(j)
#     print(type(j))
#     print(type(d))
#
# def readYaml():
#     pass

#
# class Huice:
#     a = 100
#     def test(self):
#         self.a = 300
#
# h = Huice()
# h.a = 1000
# print(h.a)
#
# print(Huice.a)


if __name__ == '__main__':
    # db类
    config1 = Config()
    print(config1.host)

    # json解析类
    config2 = Config()


    print(config2.host)

