import allure
def report(data, result):
    """
    生成定制报告
    :param data: 测试用例信息
    :param result: 实际执行结果
    :return:
    """

    url = data.get('desc').get('url')
    method = data.get('desc').get('method')

    allure.dynamic.severity(data.get('desc').get('severity'))
    allure.dynamic.story(data.get('desc').get('module'))
    allure.dynamic.title(data.get('desc').get('title'))
    allure.dynamic.suite(data.get('desc').get('module'))

    allure.dynamic.description(f'请求url：<font color=“red”>{method}: {url}</font><br/>'
                               f'实际结果：{result}<br/>')
