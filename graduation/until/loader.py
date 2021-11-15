import csv
import json
import yaml
from typing import Text, Dict, List
from loguru import logger


def load_yaml_file(yaml_file: Text) -> Dict:
    with open(yaml_file, mode='rb') as fp:
        try:
            yaml_content = yaml.load(fp, yaml.Loader)
        except yaml.YAMLError as e:
            logger.error(e)
        return yaml_content


def load_json_file(json_file: Text) -> Dict:
    with open(json_file, mode='rb') as fp:
        try:
            json_content = json.load(fp)
        except json.JSONDecodeError as e:
            logger.error(e.msg)
        return json_content


def load_csv_file(csv_file: Text) -> List[Dict]:
    """
    Examples:
    # >>> cat csv_file
    username,email,password
    huice001,65132090@qq.com,pwd001
    huice002,123456@qq.com,pwd002
    # >>> load_csv_file(csv_file)
    [
        {'username':'huice001','email':'65132090@qq.com','password':'pwd001'},
        {'username':'huice002','email':'123456@qq.com','password':'pwd002'}
    ]
    :param csv_file:
    :return:
    """
    # try  exception

    csv_content_list = []
    with open(csv_file, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            csv_content_list.append(row)

    return csv_content_list


if __name__ == '__main__':
    d = load_yaml_file('../data/testcase.yml')
    base_url = d.get('config').get('base_url')
    for item in d.get('teststeps'):
        print(item)
