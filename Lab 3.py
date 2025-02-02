class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга \"{self._name}\". Автор: {self._author}" # Добавил символы кавычек \" в названии книги

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

class PaperBook(Book):
    """ Бумажная книга (дочерний класс) """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Число страниц должно быть выражено целым числом!")
        if value < 0:
            raise ValueError("Число страниц не может быть отрицательным!")
        self._pages = value

    def __str__(self):
        return f"Книга \"{self._name}\". Автор: {self._author}. Количество страниц: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"

class AudioBook(Book):
    """ Аудиокнига (дочерний класс) """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, float):
            raise TypeError("Продолжительность должна быть выражена вещественным числом!")
        if value < 0:
            raise ValueError("Продолжительность не может быть отрицательной!")
        self._duration = value

    def __str__(self):
        return f"Книга \"{self._name}\". Автор: {self._author}. Продолжительность: {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration!r})"


print(Book("Записки книготорговца", "Шон Байтелл"))
print(PaperBook("Записки книготорговца", "Шон Байтелл", 380))
print(AudioBook("Записки книготорговца", "Шон Байтелл", 3.5))

"""
Использование print'ов, вероятно, не самая лучшая практика (по сравнению с doctest'ами).
Однако она наиболее простая по модификации классов, их методов и свойств.
Значения _name и _author сделаны protected.
Обработка значений pages и duration на корректность работает исправно.
Перегрузка методов __str__ и __repr__ вызвала лёгкое недоумение: если задокументировать один из методов,
то будет работать другой (как будто эта пара методов работает, поддерживая друг друга в отсутствие). 
"""