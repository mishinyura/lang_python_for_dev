from pydantic import BaseModel, field_validator
from exceptions import BookNotAvailable, LibraryEmpty
import re

class Book(BaseModel):
    title: str
    author: str
    year: int
    available: bool
    categories: list[str]

    def __str__(self):
        return self.title

    def __repr__(self):
        data = '(%s, %s, %s)' % (self.title, self.author, self.year)
        return data

    def __hash__(self):
        return hash(Book.__repr__(self))

class User(BaseModel):
    name: str
    email: str
    membership_id: str

    @field_validator('email')
    def email_valid(cls, data: str):
        domain_zone = ['ru', 'com', 'net', 'su']
        is_zone = re.findall(r'\.(\w+)\Z', data)[0] in domain_zone
        if '@' not in data or not is_zone:
            raise ValueError('Email is not correct')
        return data

class Library:
    def __init__(self):
        self.books = []
        self.users = {}

    def add_book(self, book: Book):
        """Добавляет в коллекцию библиотеки новую книгу
        :param book:
        :return:
        """
        self.books.append(book)

    def find_book(self) -> Book:
        """Ищет книгу в библиотеке
        :param book:
        :return:
        """
        self.total_books(True)
        while True:
            try:
                index = int(input('Введите номер книги: '))
            except ValueError:
                print('\n---Введите номер---')
            else:
                return self.books[index]

    def is_book_borrow(self, user: User):
        """Отдает книгу
        :param book:
        :return:
        """
        book = self.find_book()
        if not book:
            raise BookNotAvailable('Нет в наличии такой книги. Посмотрите доступные книги')
        book.available = False
        self.users[book] = user
        print(self.users)
        # return book

    def return_book(self, user: User) -> None:
        """Возвращает книгу в библиотеку
        :param book:
        :return:
        """
        print('№\tКнига')
        books = [book for book, usr in self.users.items() if usr == user]
        for book_idx, book in enumerate(books):
            print('%s\t%s' % (book_idx, book))
        while True:
            try:
                index = int(input('Какую книгу возращаете?: '))
            except ValueError:
                print('\n---Введите номер---')
            else:
                self.users.pop(books[index])
                books[index].available = True
                break

    def total_books(self, available: bool=False):
        if not self.books:
            raise LibraryEmpty
        print('№\tКнига')
        for book_idx, book in enumerate(self.books):
            if available and not book.available:
                continue
            print('%s\t%s' % (book_idx, book))
