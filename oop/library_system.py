class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Ebook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count):
         super().__init__(title, author)
         self.page_count = page_count

class Library(Book):
    def __init__(self, ad
      