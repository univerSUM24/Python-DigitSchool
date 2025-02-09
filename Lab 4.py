import random
import doctest
from typing import Union

"""Базовый класс Семьи"""
class Family:
    """
    Класс члена Семьи
    Метод dream наследуется из базового класса Family

    >>> person = Family('Владимир', 20)
    >>> person.name
    'Владимир'
    >>> person.age
    20
    >>> "Владимир мечтает о чём-то интересном" in person.dream(person.name)
    True
    """
    def __init__ (self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Имя: {self.name}. Возраст: {self.age}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r})"

    def dream(self, name: str) -> str:
        random_year = 2025 + random.randint(1, 10)
        return f"{name} мечтает о чём-то интересном. Надеюсь, мечта сбудется в {random_year} году!"

"""Дочерний класс Родителей (Второе поколение)"""
class Parent(Family):
    """
    Класс Родителя с работой
    Метод dream наследуется из базового класса Family

    >>> parent = Parent('Ангелина', 28, 'Архитектор')
    >>> parent.name
    'Ангелина'
    >>> parent.age
    28
    >>> parent.work
    'Архитектор'
    >>> parent.work = 'Модельер'
    >>> parent.work
    'Модельер'
    >>> parent.work = 13
    TypeError: Работа должна быть строкой!
    >>> print(parent)
    Имя: Ангелина, Возраст: 28, Работа: Модельер
    >>> repr(parent)
    "Parent(name='Ангелина', age=28, work='Модельер')"
    >>> "Ангелина мечтает о чём-то интересном" in parent.dream(parent.name)
    True
    """
    def __init__(self, name: str, age: int, work: str):
        super().__init__(name, age)
        self._work = work # Работа сделана непубличной (protected) для сохранения её целостности

    @property
    def work(self):
        return self._work

    @work.setter
    def work(self, value):
        if not isinstance(value, str):
            raise TypeError("Работа должна быть строкой!")
        self._work = value

    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Работа: {self.work}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r}, work={self.work!r})"

"""Дочерний класс Детей (Третье поколение)"""
class Children(Family):
    """
    Класс Ребёнка с увлечением
    Метод dream наследуется из базового класса Family

    >>> children = Children('Вячеслав', 5, 'Конструктор')
    >>> children.name
    'Вячеслав'
    >>> children.age
    5
    >>> children.hobby
    'Конструктор'
    >>> children.hobby = 'Мячик'
    >>> children.hobby
    'Мячик'
    >>> children.hobby = 9
    TypeError: Увлечение должно быть строкой!
    >>> print(children)
    Имя: Вячеслав, Возраст: 5, Увлечение: Мячик
    >>> repr(children)
    "Children(name='Вячеслав', age=5, hobby='Мячик')"
    >>> "Вячеслав мечтает о чём-то интересном" in children.dream(children.name)
    True
    """
    def __init__(self, name: str, age: int, hobby: str):
        super().__init__(name, age)
        self._hobby = hobby # Увлечение сделано непубличным (protected) для сохранения его целостности

    @property
    def hobby(self):
        return self._hobby

    @hobby.setter
    def hobby(self, value):
        if not isinstance(value, str):
            raise TypeError("Увлечение должно быть строкой!")
        self._hobby = value

    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Увлечение: {self.hobby}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r}, hobby={self.hobby!r})"

"""Дочерний класс Прародителей (Первое поколение)"""
class Grandparent(Family):
    """
        Класс Прародителя с увлечением
        Метод dream наследуется из базового класса Family

        >>> grandparent = Grandparent('Евгения', 51, 21000)
        >>> grandparent.name
        'Евгения'
        >>> grandparent.age
        51
        >>> grandparent.pension
        21000
        >>> grandparent.pension = 19500
        >>> grandparent.pension
        19500
        >>> grandparent.pension = 'Двадцать две тысячи'
        TypeError: Пенсия - это число!
        >>> print(grandparent)
        Имя: Евгения, Возраст: 51, Пенсия: 19500
        >>> repr(grandparent)
        "Grandparent(name='Евгения', age=51, pension=19500)"
        >>> "Евгения мечтает о чём-то интересном" in grandparent.dream(grandparent.name)
        True
        """
    def __init__(self, name: str, age: int, pension: Union[int, float]):
        super().__init__(name, age)
        self._pension = pension # Пенсия сделана непубличной (protected) для сохранения её целостности

    @property
    def pension(self):
        return self._pension

    @pension.setter
    def pension(self, value):
        if not isinstance(value, Union[int,float]):
            raise TypeError("Пенсия - это число!")
        self._pension = value

    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Пенсия: {self.pension}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r}, pension={self.pension!r})"

if __name__ == "__main__":
    doctest.testmod()
    pass