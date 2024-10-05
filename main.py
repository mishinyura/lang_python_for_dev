from math import sqrt

class NumberEvenError(Exception):
    def __init__(self):
        self.message = 'Найдено четное чисто'

    def __str__(self):
        return self.message

class NumberNegativeError(Exception):
    def __init__(self):
        self.message = 'Найдено отрицательное чисто'

    def __str__(self):
        return self.message

def processing_division_zero_and_receiving_str(f_num: int, s_num: int) -> None:
    """Функция принимает два числа от пользователя и выводит результат их деления
    :param f_num: int делимое
    :param s_num: int делитель
    :return: None. Выводит результат на экран
    """
    try: print(f_num / s_num)
    except ZeroDivisionError as ex: print(ex)
    except TypeError as ex: print(ex)

# @timer
def sum_list(lst: list|tuple) -> None:
    """Функция вычисляет сумму списка целых чисел.
    :param lst: список или кортеж
    :return: None. Выводит результат на экран
    """
    try:
        if len([num for num in lst if num % 2 == 0]): raise NumberEvenError()
        elif len([num for num in lst if num < 0]): raise NumberNegativeError()
    except NumberEvenError as ex: print(ex)
    except NumberNegativeError as ex: print(ex)
    else: print(sum(lst))

def processing_index_error(index: int) -> None:
    """Функция принимает от пользователя индекс элемента списка и выводит
    значение этого элемента.
    :param index: int  целой число как отрицательное, так и положительное
    :return: None. Выводит результат на экран
    """
    lst = [1, 2, 3, 4, 5]
    try: print(lst[index])
    except IndexError as ex: print(ex)

def convert_str_to_num(string: str) -> None:
    """Функция принимает от пользователя строку и преобразует её в число с плавающей точкой
    :param string: строка, которуб нужно преобразовать
    :return: None. Выводит результат на экран
    """
    try: print(float(string))
    except ValueError as ex: print(ex)


def import_module(num: int) -> None:
    """Функция принимает число и вычисляет квадратный корень этого числа
    :param num: чисто в квадрате
    :return: None. Выводит результат на экран
    """
    try: print(sqrt(num))
    except ValueError as ex: print(ex)
    except TypeError as ex: print(ex)


def main():
    processing_division_zero_and_receiving_str('dd', 0)
    sum_list([-1, 0, 1, 2, 3])
    processing_index_error(6)
    convert_str_to_num('12ц')
    import_module(-9)

if __name__ == '__main__':
    main()