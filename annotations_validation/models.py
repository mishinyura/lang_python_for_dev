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
    books: list[Book] = []

    @field_validator('email')
    def email_valid(cls, data: str):
        if '@' not in data:
            raise ValueError('Email is not correct')
        return data

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book: Book) -> None:
        index = self.books.index(book)
        self.books.pop(index)

    def print_books(self):
        print('№\tКнига')
        for book_idx, book in enumerate(self.books):
            print('%s\t%s' % (book_idx, book))

class Library:
    def __init__(self) -> None:
        self.books = []
        self.users = {}

    def add_book(self, book: Book) -> None:
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

    def is_book_borrow(self, user: User) -> Book:
        """Отдает книгу пользователю и выводит.
        :param user: Пользователь, который хочет одолжить книгу
        :return: экземпляр класса книги
        """
        book = self.find_book()
        if not book:
            raise BookNotAvailable('Нет в наличии такой книги. Посмотрите доступные книги')
        book.available = False
        self.users[book] = user
        return book

    def return_book(self, user: User) -> Book:
        """Возвращает книгу в библиотеку.
        :param user: Пользователь, который возвращает книгу
        :return: Выводит результат на экран
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
                print('\n---Спасибо, что во время вернули---')
                return books[index]

    def total_books(self, available: bool=False) -> None:
        """Выводит список книг, имеющихся в библиотеке
        :param available: True - показывает только свободные,
        иначе показывает все книги
        :return: Выводит результат на экран
        """
        if not self.books:
            raise LibraryEmpty
        print('№\tАвтор\t\tГод\tКнига')
        for book_idx, book in enumerate(self.books):
            if available and not book.available:
                continue
            print('%s\t%s\t%s\t%s' % (book_idx, book.author, book.year, book))
