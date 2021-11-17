import requests

from graduation.apiRunner.testcase import RunRequest

base_url ="https://www.jianshu.com/p/932a4d9f78f8/"
# session = requests.session()
# data = {"fastloginfield":'username',
#         "username":"huice0008",
#         "password":"huice0008",
#         "quickforward":"yes",
#         "handlekey":"ls"
#
# }
# headers ={"Content-Type","application/x-www-form-urlencoded"}

req = RunRequest('步骤一，登录')
step = req.get(base_url)
print(req)
# step_dict =step.request.dict()
# session.request()
