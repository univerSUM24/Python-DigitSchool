import doctest
import math
import random
from typing import Union

class ComplexNumbers:
    def __init__ (self, real_part, imagine_part):
        self.real_part = real_part # На действительную часть комплексного числа жизнь не накладывает никаких ограничений
        self.imagine_part = imagine_part # На мнимую часть комплексного числа жизнь не накладывает никаких ограничений

    # Метод класса ComplexNumbers для вычисления модуля (длины вектора) комплексного числа
    # Аргументы - вещественные числа
    def length_of_vector(self, real_part, imagine_part):
        if not (isinstance(real_part, Union[float, int]) or isinstance(imagine_part, Union[float, int])):
            raise TypeError("Аргументы комплексного числа - числа!") # Вызов ошибки при некорректном вводе аргументов
        length = math.sqrt(math.pow(real_part, 2) + math.pow(imagine_part, 2))
        return length

class StudentsGroup:
    def __init__ (self, count_of_students):
        if not isinstance(count_of_students, int):
            raise TypeError("Число студентов должно быть выражено целым числом!") # Вызов ошибки при некорректном числе студентов
        if count_of_students < 0:
            raise ValueError("Число студентов должно быть неотрицательным!")  # Вызов ошибки при некорректном числе студентов
        self.count_of_students = count_of_students

    # Метод класса StudentsGroup для случайного выбора студента для выхода к доске
    def go_to_desk_rand(self, count_of_students):
        rand_student = int(random.randint(0, count_of_students))
        return rand_student

class NewYearGifts:
    def __init__ (self, list_of_gifts: dict):
        self.list_of_gifts = list_of_gifts

    # Метод класса NewYearGifts для вычисления итоговой суммы для подарков
    def total_budget(self, list_of_gifts: dict):
        total_sum = sum(list_of_gifts.values())
        return total_sum


if __name__ == "__main__":

    complex_num = ComplexNumbers(3,4)
    print(complex_num) # Вывод принадлежности к классу ComplexNumbers
    #help(complex_num)
    length = complex_num.length_of_vector(complex_num.real_part, complex_num.imagine_part)
    print(length) # Результат работы метода length_of_vector() класса ComplexNumbers

    group_of_students = StudentsGroup(30)
    print(group_of_students) # Вывод принадлежности к классу StudentsGroup
    #help(group_of_students)
    rand_student = group_of_students.go_to_desk_rand(group_of_students.count_of_students)
    print(rand_student) # Результат работы метода go_to_desk_rand() класса StudentsGroup

    # Список подарков на Новый год
    list_of_gifts = {
        'Мандарины': 240,
        'Плюшевый медвежонок': 570,
        'Духи': 4500
    }
    NewYearsSheet = NewYearGifts(list_of_gifts) # Инициализация экземпляра класса NewYearGifts
    print(NewYearsSheet) # Вывод принадлежности к классу NewYearGifts
    #help(NewYearsSheet)
    total_gift_budget = NewYearsSheet.total_budget(NewYearsSheet.list_of_gifts)
    print(total_gift_budget) # Результат работы метода total_budget() класса NewYearGifts

    doctest.testmod()
    pass