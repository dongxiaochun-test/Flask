import re
from typing import Any, Text, Union

"""
断言组件
"""


def equal(check_value: Any, expect_value: Any, message: Text = ''):
    assert check_value == expect_value, message


def not_equal(check_value: Any, expect_value: Any, message: Text = ''):
    assert check_value != expect_value, message


def greater_than(check_value: Union[int, float], expect_value: Union[int, float], message: Text = ''):
    assert check_value > expect_value, message


def less_than(check_value: Union[int, float], expect_value: Union[int, float], message: Text = ''):
    assert check_value < expect_value, message


def greater_or_equal(check_value: Union[int, float], expect_value: Union[int, float], message: Text = ''):
    assert check_value >= expect_value, message


def less_equal(check_value: Union[int, float], expect_value: Union[int, float], message: Text = ''):
    assert check_value <= expect_value, message


def length_equal(check_value: Text, expect_value: int, message: Text = ''):
    assert isinstance(expect_value, int), 'expect_value 必须是int类型'
    assert len(check_value) == expect_value, message


def length_greater_equal(check_value: Text, expect_value: Union[int, float], message: Text = ''):
    assert isinstance(expect_value, (int, float)), 'expect_value 必须是int或者float类型'
    assert len(check_value) > expect_value, message


def contains(check_value: Any, expect_value: Any, message: Text = ''):
    assert expect_value in check_value, message


def startwith(check_value: Any, expect_value: Any, message: Text = ''):
    str(check_value).startswith(str(expect_value)), message


def endwith(check_value: Any, expect_value: Any, message: Text = ''):
    str(check_value).endswith(str(expect_value)), message


def regex_match(check_value: Text, expect_value: Any, message: Text = ''):
    assert re.match(check_value, expect_value), message
