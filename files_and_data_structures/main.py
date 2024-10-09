from utils import timer
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
@timer
def sum_order(path: str) -> int:
    with open(path, 'r', encoding='utf-8') as file:
        result = sum(map(int, [i.strip().split('\t')[2] for i in file.readlines()]))
        return result


@timer
def sum_order2(path: str) -> int:
    with open(path, 'r', encoding='utf-8') as file:
        result = sum(list(map(int, re.findall(r'\d+\n', file.read()))))
        return result

@timer
def counter_words(path: str) -> int:
    with open(path, 'r', encoding='utf-8') as file:
        return len(re.findall(r'\w+.?', file.read()))

def main():
    # write_copy_file('data/source.txt', 'results/destination.txt')
    # print(sum_order('data/prices.txt'))
    # print(sum_order2('data/prices.txt'))
    counter_words('data/text_file.txt')

if __name__ == '__main__':
    main()
    #0.0009982585906982422
