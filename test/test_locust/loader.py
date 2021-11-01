import csv
from typing import Text, List, Dict


def load_csv_file(csv_file: Text) -> List[Dict]:
    """
    csv_file文件格式举例：
        email,password
        65132090@qq.com,123456
        65132091@qq.com,123456
    返回的数据格式举例：
        [
            {'email':'65132090@qq.com','password':'123456'},
            {'email':'65132091@qq.com','password':'123456'}
        ]
    :param csv_file:
    :return:
    """
    csv_content_list = []
    with open(csv_file, encoding='utf-8') as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            csv_content_list.append(row)
    return csv_content_list


if __name__ == '__main__':
    csv_content_list = load_csv_file('./data/user.csv')
    for item in csv_content_list:
        print(item.get('email'))
        print(item.get('password'))
