#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from bob.bob import Person


class Salesclerk(Person):
    def __init__(self, name):
        super().set_name(name)

if __name__ == '__main__':
    pass
