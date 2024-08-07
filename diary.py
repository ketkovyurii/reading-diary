import datetime
from book import Book
from typing import List, Set


class Diary:
    def __init__(self) -> None:
        self.books: List[Book] = []

        print("\ndiary instance had been created\n")

    def clear(self) -> None:
        self.books.clear()

        print("\n- diary has been cleared\n")

    def delete_diary(self) -> None:
        self.books = []

        print("\n- diary has been deleted\n")

    def add(self, book: Book) -> None:
        self.books.append(book)

    def __str__(self) -> str:
        return "".join(
            "#{}\n{}\n\n".format(i, self.books[i]) for i in range(len(self.books))
        )

    def write_to_file(self, file_name: str) -> None:
        file1 = open(file_name, "w")
        file1.write(str(self))
        file1.close()
        print("\n- the diary has been written into the file `{}\n`".format(file_name))

    def read_from_file(self, file_name: str) -> None:
        with open(file_name, "r") as file:
            data = file.read()

        entries = data.strip().split("\n\n")

        for entry in entries:
            lines = entry.strip().split("\n")
            author = lines[1].split(": ")[1].strip()
            title = lines[2].split(": ")[1].strip()
            genre = set(lines[3].split(": ")[1].strip().split(", "))
            year = int(lines[4].split(": ")[1].strip())
            pages = int(lines[5].split(": ")[1].strip())
            date_of_completion = datetime.datetime.strptime(
                lines[6].split(": ")[1].strip(), "%Y-%m-%d"
            )

            book = Book(author, title, genre, year, pages, date_of_completion)
            self.add(book)

        print("the file `{}` has been read to the diary\n".format(file_name))
        file.close()

    def find_by_title(self, title: str) -> None:
        for i, book in enumerate(self.books):
            if book.title == title:
                print(
                    "the book with title `{}` has been found:\n\n{}".format(
                        title, str(book)
                    )
                )

                return

        print("the book `{}` has not been found\n".format(title))
        return

    def remove_by_title(self, title: str) -> None:
        for i, book in enumerate(self.books):
            if book.title == title:
                print("the book `{}` has been removed from the diary\n".format(title))
                del self.books[i]

                return
        print("the book is not in the diary\n")
        return

    def find_by_author(self, author: str) -> None:
        k = 0

        for book in self.books:
            if book.author == author:
                k += 1

                if k == 1:
                    print("- here are the books of author `{}`:\n".format(author))

                print(str(book))

        if k == 0:
            print("- no books of author `{}` has been found\n".format(author))
            return

        else:
            return

    def remove_by_author(self, author: str) -> None:
        k = 0
        for i, book in enumerate(self.books):
            if book.author == author:

                k += 1
                print("- book `{}` has been removed\n".format(book.title))
                del self.books[i]

        if k == 0:
            print("- no books with author `{}` has been found\n".format(author))
            return
