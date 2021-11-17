import requests

class Client:
    def __init__(self, url, method, type=0):
        self.url = url
        self.method = method
        self.type = type
        self.header ={}
        self.data = {}
        self.res = None


    def set_header(self,key,value):
        self.header[key] =value

    def set_data(self,dic):
        if isinstance(dic,dict):
            self.data = dic
        else:
            raise Exception("请求参数以字典格式传递")

    def send(self):
        if self.method =="GET":
            self.res=requests.get(url=self.url,headers =self.header,params=self.data)
        elif self.method =="POST":
            if self.type == 1:
                self.res=requests.post(url=self.url,headers =self.header,data=self.data)
            elif self.type ==5:
                self.res=requests.post(url=self.url, headers=self.header, data=self.data)
            elif self.type ==2:
                self.header("Content-Type","application/x-www-form-urlencoded")
                self.res=requests.post(url=self.url, headers=self.header, data=self.data)
            elif self.type ==3:
                self.header("Content-Type", "text/xml")
                xml = self.data.get("xml")
                if xml:
                    self.res=requests.post(url=self.url, headers=self.header, data=self.data)
                else:
                    raise Exception("xml正文，入参格式：{"":""}")
            elif self.type ==4:
                self.set_header("Content-Type", "application/json")
                self.res = requests.post(url=self.url, headers=self.header, json =self.data)

            elif self.type == 0:
                self.res = requests.post(url=self.url, headers=self.header)
            else:
                raise Exception("type传入错误")

        else:
            raise Exception("请求方式暂时不支持")



class Method:
    GET = "GET"
    POST = "POST"

class Type:
    FROM = 1
    URL_ENCODE = 2
    XML = 3
    JSON = 4
    FILE =5