#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from bob.bob import Person


class Dad(Person):
    __childrens: list[Person] = []

    def __init__(self, name):
        super().set_name(name)

    def add_childrens(self, children: Person):
        self.__childrens.append(children)

    def get_childrens(self) -> str:
        return self.__childrens

if __name__ == '__main__':
    pass
