import re
def write_copy_file(i_path: str, o_path: str) -> None:
    """Функция копирует данные из одного файла и вставляет во второй
    :param i_path: input path, пусть файла с исходными данными
    :param o_path: output path, пусть файла с полученными данными
    :return: None. Результат записывается в файл
    """
    with open(i_path, 'r', encoding='utf-8') as i_file:
        with open(o_path, 'w', encoding='utf-8') as o_file:
            o_file.write(i_file.read())

def sum_order(path: str) -> int:
    """Функция считает сумму заказа из файла.
    :param path: Пусть до файла
    :return: Сумма заказа
    """
    with open(path, 'r', encoding='utf-8') as file:
        result = sum(map(int, re.findall(r'\d+\n', file.read())))
        return result


def counter_words(path: str) -> None:
    """Функция считает количество слов в файле
    :param path: Пусть до файла
    :return: None. Результат выводит на экран
    """
    with open(path, 'r', encoding='utf-8') as file:
        print(len(re.findall(r'\w+.?', file.read())))

def search_unique_line(i_path: str, o_path: str) -> None:
    """Функция копирует данные из одного файла и вставляет уникальные строки во второй
    :param i_path: input path, пусть файла с исходными данными
    :param o_path: output path, пусть файла с полученными данными
    :return: None. Результат записывается в файл
    """
    with open(i_path, 'r', encoding='utf-8') as i_file:
        with open(o_path, 'w', encoding='utf-8') as o_file:
            data = {line for line in i_file.readlines()}
            o_file.write(*data)

def main():
    write_copy_file('data/source.txt', 'results/destination.txt')
    print(sum_order('data/prices.txt'))
    counter_words('data/text_file.txt')
    search_unique_line('data/input.txt', 'results/unique_output.txt')

if __name__ == '__main__':
    main()
