import unittest
from xml.etree import ElementTree as ET

if __name__ == '__main__':

    et = ET.parse('./config.xml')
    li = et.findall('./cases/*')

    suit = unittest.TestSuite()

    for i in li:
        class_name = i.tag.split('-')[0]
        method_name = i.tag.split('-')[1]

        exec('imp')
