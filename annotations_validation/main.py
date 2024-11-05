from models import Book, User, Library
from data import book1, book2, book3, book4
import os

def create_book():
    data = {
        "title": input('Название книги: '),
        "author": input('Автор: '),
        "year": int(input('Год выпуска: ')),
        "available": True,
        "categories": input('Перечислите категории книги через запятую: ').split(', ')
    }
    book = Book(**data)
    return book

def select():
    welcome = ('\nДоступные действия:'
               '\n\t1. Показать все книги'
               '\n\t2. Показать книги в наличии'
               '\n\t3. Подарить книгу библиотеке'
               '\n\t4. Взять книгу'
               '\n\t5. Вернуть книгу'
               '\n\t6. Показать мои книги\n')
    while True:
        try:
            select = int(input(welcome))
        except ValueError:
            print('\n---Укажите цифру действия---')
        else:
            return select

def main():
    lib = Library()

    print(f'Добро пожаловать в Библотеку!\n{"_" * 50}')
    while True:
        print('Для продоления, введите ваши данные:')
        try:
            name = input('Имя: ')
            email = input('Email: ')
            user = User(name=name, email=email, membership_id='test')
        except ValueError as ex:
            print(f'Ошибка: {ex}')
        else:
            books = book1, book2, book3, book4
            for book in books:
                obj = Book(**book)
                lib.add_book(obj)
            break
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        s = select()
        print(s)
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            match s:
                case 1: lib.total_books()
                case 2: lib.total_books(True)
                case 3: lib.add_book(create_book())
                case 4:
                    book = lib.is_book_borrow(user)
                    user.add_book(book)
                case 5:
                    book = lib.return_book(user)
                    user.remove_book(book)
                case 6: print(user.books)
                case _: print('\n---Выберете действие из предложенных---')
        except Exception as ex:
            print(ex)




if __name__ == '__main__':
    main()