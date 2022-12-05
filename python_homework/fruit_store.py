#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from bob.bob import Store


class FruitStore(Store):
    def __init__(self, goods, num, store_name="水果店"):
        self.storeName = store_name
        self.goods = goods
        self.num = num

if __name__ == '__main__':
    pass
