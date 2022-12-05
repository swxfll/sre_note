#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from bob.alice import Alice
from bob.bob import Bob
from bob.bread_store import BreadStore
from bob.dad import Dad
from bob.fruitBaskets import FruitBaskets
from bob.fruit_store import FruitStore
from bob.salesclerk import Salesclerk

# 新建人物并确认关系
bob = Bob("鲍勃")
alice = Alice("爱丽丝")
dad = Dad("鲍勃的爸爸")
dad.add_childrens(bob)
dad.add_childrens(alice)

# 鲍勃的爸爸生病了,住进了医院
dad.set_state("生病了")
dad.set_location("医院")

# 爱丽丝去买东西
salesclerk = Salesclerk("售货员")
fruitBaskets = FruitBaskets(salesclerk.get_name())
fruitBaskets.put(BreadStore("热狗", 3)).put(FruitStore("苹果", 9)).put(FruitStore("橙子", 6))
fruitBaskets.set_owner(alice.get_name())

fruitBaskets.printItem()

# 鲍勃开车
bob.drive()

# 爱丽丝将果篮递到鲍勃的手中
fruitBaskets.set_owner(bob.get_name())

# 爱丽丝从其中一个果篮中拿了一个苹果
fruitBaskets.take("苹果", 1)

if __name__ == '__main__':
    pass
