![image](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/temp/bob.png)

```py
-------------------------------------------------------------------------------------------
filename:  alice_dad.py
-------------------------------------------------------------------------------------------
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from person import Person


class AliceDad(Person):

    __childrens: list[Person] = []

    def __init__(self, name):
        super().set_name(name)

    def add_childrens(self, children: Person):
        self.__childrens.append(children)

    def get_childrens(self) -> list[Person]:
        return self.__childrens

if __name__ == '__main__':
    pass



-------------------------------------------------------------------------------------------
filename:  bakery.py
-------------------------------------------------------------------------------------------
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from shop import Shop


class Bakery(Shop):
    """
    面包店
    """
    pass


if __name__ == '__main__':
    pass



-------------------------------------------------------------------------------------------
filename:  box.py
-------------------------------------------------------------------------------------------
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from bread import Bread
from fruit import Fruit
from item import Item
from person import Person


class Box(Item):
    """
    果篮子
    """
    __items: list[Item] = []
    __name: str = None

    # 拥有者
    __owner: Person = None
    __last_owner: Person = None

    def __init__(self, name) -> None:
        self.__items = []
        self.__name = name

    def put_box(self, item: Item) -> None:
        self.__items.append(item)

    def get_item(self) -> Item:
        return self.__items

    def set_owner(self, person) -> None:
        if self.__name is not None:
            self.__last_owner = self.__owner
        self.__owner = person

    def get_owner(self) -> Person:
        return self.__owner

    def get_last_owner(self) -> Person:
        return self.__last_owner

    def printBox(self) -> None:
        for i in self.__items:
            print(i)


if __name__ == '__main__':
    pass



-------------------------------------------------------------------------------------------
filename:  bread.py
-------------------------------------------------------------------------------------------
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from item import Item


class Bread(Item):
    """
    面包
    """

    # 口味
    __taste = None

    def __init__(self, name: str, num: int, taste: str) -> None:
        super().set_name(name)
        super().set_num(num)
        self.__taste = taste

    def __str__(self):
        return f"面包名: {self.get_name()}, 数量: {self.get_num() }"




if __name__ == '__main__':
    pass



-------------------------------------------------------------------------------------------
filename:  building.py
-------------------------------------------------------------------------------------------
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Building:
    """
    建筑
    """
    __company = None
    __address = None
    __area = None

    def get_area(self) -> int:
        pass

    def set_area(self, x: int, y: int):
        if x < 0 or y < 0:
            self.__area = 0
        else:
            self.__area = x * y


if __name__ == '__main__':
    pass



-------------------------------------------------------------------------------------------
filename:  car.py
-------------------------------------------------------------------------------------------
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from person import Person


class Car:
    """
    车
    """
    __brand = None
    __driver = None

    # 乘客
    __passengers: Person = []

    def __init__(self, brand: str, driver: Person = None) -> None:
        self.__brand = brand
        self.__driver = driver

    def remove_passenger(self, p: Person):
        self.__passengers.remove(p)

    def add_passenger(self, p: Person):
        self.__passengers.append(p)

    def set_passenger(self, p: Person):
        self.__passengers = []
        self.__passengers.append(p)

    def get_passenger(self):
        print(self.__passengers)

    def get_driver(self) -> Person:
        return self.__driver

    def set_driver(self, p: Person):
        self.__driver = p

    def run(self):
        if self.__driver is not None:
            print("{driver_name} 正在驾驶 {brand} 车,乘客有{passengers}...".format(
                driver_name=self.__driver.get_name(),
                brand=self.__brand,
                passengers=self.__passengers))


if __name__ == '__main__':
    pass



-------------------------------------------------------------------------------------------
filename:  fruit.py
-------------------------------------------------------------------------------------------
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from item import Item


class Fruit(Item):
    """
    水果
    """

    # 气候
    __climate = None

    def __init__(self, name: str, num: int, climate: str) -> None:
        super().set_name(name)
        super().set_num(num)
        self.__climate = climate

    def __str__(self):
        return f"水果名: {self.get_name()}, 数量: {self.get_num() }"


if __name__ == '__main__':
    pass



-------------------------------------------------------------------------------------------
filename:  fruit_store.py
-------------------------------------------------------------------------------------------
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from shop import Shop


class FruitStore(Shop):
    """
    水果店
    """
    pass


if __name__ == '__main__':
    pass



-------------------------------------------------------------------------------------------
filename:  hospital.py
-------------------------------------------------------------------------------------------
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from building import Building
from person import Person


class Hospital(Building):
    """
    医院
    """
    __master = None
    __level = None
    __name = None
    __items: list[Person] = []

    def __init__(self, name) -> None:
        self.__name = name

    def add_item(self, item: Person) -> None:
        self.__items.append(item)

    def get_item(self) -> list[Person]:
        return self.__items



if __name__ == '__main__':
    pass



-------------------------------------------------------------------------------------------
filename:  item.py
-------------------------------------------------------------------------------------------
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from person import Person


class Item:
    """
    物品
    """
    __type = None
    __name = None
    __price = None
    __owner: Person = None
    __num = 0

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def get_owner(self) -> Person:
        return self.__owner

    def set_owner(self, person: Person) -> None:
        self.__owner = person

    def set_num(self, num: int) -> None:
        if num < 0:
            self.__num = 0
        else:
            self.__num = num

    def get_num(self) -> int:
        return self.__num

    def __repr__(self) -> str:
        return f"name:{self.__name}, num:{self.__num}"


if __name__ == '__main__':
    pass



-------------------------------------------------------------------------------------------
filename:  main.py
-------------------------------------------------------------------------------------------
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

from alice_dad import AliceDad
from box import Box
from bread import Bread
from car import Car
from fruit import Fruit
from hospital import Hospital
from person import Person


def application():
    bob = Person(name="Bob")
    alice = Person(name="Alice")
    alice_dad = AliceDad(name="Alice's dad")
    # 鲍勃的爸爸
    alice_dad.add_childrens(bob)

    # 鲍勃的爸爸生病了,住进了医院
    hospital = Hospital(name="医院")
    hospital.add_item(alice_dad)

    # 爱丽丝去买水果
    bread = Bread(name="热狗", num=3, taste="咸的")
    apple = Fruit(name="苹果", num=9, climate="温带")
    orange = Fruit(name="橙子", num=6, climate="热带")

    boxs: list[Box] = []
    print("==========果篮1==============")
    fruits_box = Box(name="1号水果篮")
    fruits_box.set_owner(alice)
    fruits_box.put_box(apple)
    fruits_box.put_box(orange)
    fruits_box.printBox()
    boxs.append(fruits_box)

    print("==========果篮2==============")
    bread_box = Box(name="2号水果篮")
    bread_box.set_owner(alice)
    bread_box.put_box(bread)
    bread_box.printBox()
    boxs.append(bread_box)

    # alice.add_baskets(fruits_box).add_baskets(bread_box)

    # 鲍勃开车去医院
    tesla = Car(brand="Tesla")
    tesla.set_driver(p=bob)
    tesla.add_passenger(alice)  # car 添加乘客
    tesla.run()

    # 爱丽丝将两个果篮递到鲍勃手中
    fruits_box.set_owner(bob)
    bread_box.set_owner(bob)
    # alice.remove_basket(fruits_box).remove_basket(bread_box)
    # bob.add_baskets(fruits_box).add_baskets(bread_box)

    # 爱丽丝从其中一个果篮中拿了一个苹果给爸爸
    print(fruits_box.get_item())
    for box in boxs:
        for item in box.get_item():
            if item.get_name() == "苹果":
                item.set_num(item.get_num() - 1)
                item.set_owner(alice_dad)

    print(fruits_box.get_item())

    # 爱丽丝送鲍勃离开医院
    tesla.set_driver(alice)
    tesla.set_passenger(bob)
    tesla.run()


if __name__ == "__main__":
    application()



-------------------------------------------------------------------------------------------
filename:  person.py
-------------------------------------------------------------------------------------------
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# from box import Box


class Person:
    """
    人
    """
    __name = None
    # __baskets: list[Box] = []

    def __init__(self, name: str) -> None:
        self.__baskets = []
        self.__name = name

    def set_name(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    # def add_baskets(self, box: Box):
    #     self.__baskets.append(box)
    #     return self
    #
    # def remove_basket(self, box: Box):
    #     self.__baskets.remove(box)
    #     return self
    #
    # def get_baskets(self) -> list[Box]:
    #     return self.__baskets

    def __repr__(self):
        return self.__name


if __name__ == '__main__':
    pass



-------------------------------------------------------------------------------------------
filename:  shop.py
-------------------------------------------------------------------------------------------
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from building import Building


class Shop(Building):
    """
    商店
    """
    __brand = None
    __f = None
    __name = None
    __items = []


if __name__ == '__main__':
    pass
```
