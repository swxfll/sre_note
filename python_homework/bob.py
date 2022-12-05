#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from bob.bob import Person


class Bob(Person):
    def __init__(self, name):
        super().set_name(name)

    def drive(self):
        print(f"{self.get_name()},开车")

if __name__ == '__main__':
    pass
