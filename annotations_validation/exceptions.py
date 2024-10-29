class BookNotAvailable(Exception):
    def __init__(self, message: str='Книга не найдена'):
        self.message = message

    def __str__(self):
        return self.message

class LibraryEmpty(Exception):
    def __init__(self, message: str='Библиотека путая'):
        self.message = message

    def __str__(self):
        return self.message