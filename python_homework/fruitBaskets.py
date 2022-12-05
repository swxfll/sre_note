#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from bob.bob import Store


class FruitBaskets:
    __owner = None
    __lists: list[Store] = []

    def __init__(self, owner):
        self.owner = owner

    def set_owner(self, owner: str):
        self.__owner = owner

    def get_owner(self) -> str:
        return self.__owner

    # 默认同一家店的物品放同一个篮子里
    def put(self, store: Store):
        flag = False
        index = 0
        for i in range(len(self.__lists)):
            if self.__lists[i]["storeName"] == store.storeName:
                flag = True
                index = i
                break
        if flag:
            self.__lists[index]["goods"][store.goods] = store.num
        else:
            self.__lists.append({"storeName": store.storeName, "goods": {store.goods: store.num}})

        return self

    def take(self, name: str, num: int):
        for item in self.__lists:
            if name in item["goods"]:
                item["goods"][name] = item["goods"][name] - num

    def printItem(self):
        print(f"{self.owner}果篮中的食物")
        for item in self.__lists:
            print(item)

if __name__ == '__main__':
    pass
