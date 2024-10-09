
def write_copy_file(i_path: str, o_path: str) -> None:
    """Функция копирует данные из одного файла и вставляет во второй
    :param i_path: input path, пусть файла с исходными данными
    :param o_path: output path, пусть файла с полученными данными
    :return: None. Результат записывается в файл
    """
    with open(i_path, 'r', encoding='utf-8') as i_file:
        with open(o_path, 'w', encoding='utf-8') as o_file:
            o_file.write(i_file.read())

def main():
    write_copy_file('data/source.txt', 'results/destination.txt')

if __name__ == '__main__':
    main()