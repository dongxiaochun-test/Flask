#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2021/9/5 15:20
# @Author:ytq
# @File:repr_demo.py


class Demo:
    pass

    def __repr__(self):
        return "demo"


if __name__ == '__main__':
    print(Demo())
