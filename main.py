from datetime import datetime
from book import *
from diary import Diary

print(
    """! welcome to Yurii Ketkov zapocet program\n\n! to check the list of all the avaliable commands type --help\n
! before using any commands, please create a diary using command --create-diary\n\n! otherwise the programm crushes\n
! there is already file `data.txt` in this directory so that the tester could save his time, you are most welcome to use it\n
! just enter --read-from-file to use author's data\n"""
)

while 1:
    user_input = input("- enter desired command\n\n")

    match user_input:
        case "--help":
            s = """\n\n\n--create-diary - creates a new empty diary\n\n--print-diary\n\n--write-to-file\n\n--read-from-file\n\n--add-book\n\n--search-by-author\n\n--search-by-title\n\n--delete-title\n\n--delete-author\n\n--clear\n\n--kill\n\n--exit\n"""
            print(s)

        case "--create-diary":
            diary = Diary()

        case "--print-diary":
            print(diary)

        case "--write-to-file":
            x = input("\n- specify the name of the file\nplease, include .txt\n")
            diary.write_to_file(x)

        case "--read-from-file":
            x = input(
                "\n- enter the name of the file from which you want to read data: "
            )
            diary = Diary()
            diary.read_from_file(x)

        case "--add-book":
            book = Book(
                input("\n- enter the author of the book: "),
                input("\n- enter the title of the book: "),
                enter_genres(),
                int(input("\n- enter the year of release: ")),
                int(input("\n- enter the number of pages: ")),
                enter_date(),
            )
            diary.add(book)
            print(
                "\n- a book `{}` has been added to the diary\nto see the full diary, enter --print-diary "
            )

        case "--search-by-author":
            diary.find_by_author(input("\n- enter the author of the book: "))

        case "--search-by-title":
            diary.find_by_title(input("\n- enter the name of the book: "))

        case "--delete-title":
            diary.remove_by_title(input("\n- enter the title of the book: "))
        case "--delete-author":
            print()
            diary.remove_by_author(input("\n- enter the name of the author: "))

        case "--clear":
            diary.clear()

        case "--kill":
            del diary
            print(
                "\n- diary has been deleted completely\nbefore you continue, create new diary with --create-diary\n\n- don't call --kill 2nd time - a program will crash"
            )

        case "--exit":
            break

        case _:
            print(
                "\n- an unknown command\nto see full list of commands, enter --help\n"
            )
