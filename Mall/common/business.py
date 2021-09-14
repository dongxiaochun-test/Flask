from request.httpclient import HttpClient
def getAuthCode(telephone = None):
    url = f'http://121.37.169.128:8201/mall-member/sso/getAuthCode?telephone={telephone}'
    # 执行
    client = HttpClient()
    result = client.get(url=url)
    return result.get('data')

if __name__ == '__main__':
   
    print(s.message)
#
# header = getAuthorization()
# print(header)