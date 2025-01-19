BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
           return f"Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})"


class Library:
    def __init__(self, books: list = None):
        self.books = books if books is not None else [] # пустой список книг

    def get_next_book_id(self) -> int:
        if not self.books:
            return 1
        return max(book.id_ for book in self.books) + 1 # всё предельно просто: находим наибольший существующий id и прибавляем 1

    def get_index_by_book_id(self, id_: int) -> int:
        try:
         index = next(index for index, book in enumerate(self.books) if book.id_ == id_)
         return index
        except StopIteration: # вызов исключения
            raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()
    print(empty_library.get_next_book_id())

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())
    print(library_with_books.get_index_by_book_id(1))