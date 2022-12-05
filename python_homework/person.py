#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Person:
    __name = None
    __state = None
    __location = None

    def set_name(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_state(self, state: str):
        self.__state = state

    def get_state(self) -> str:
        return self.__state

    def set_location(self, location: str):
        self.__location = location

    def get_location(self) -> str:
        return self.__location

if __name__ == '__main__':
    pass
