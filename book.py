import datetime


class Book:
    def __init__(
        self,
        author: str,
        title: str,
        genre: set[str],
        year: int,
        pages: int,
        date_of_completion: datetime,
    ) -> None:
        self.author = author
        self.title = title
        self.genre = genre
        self.year = year
        self.pages = pages
        self.date_of_completion = date_of_completion

    def __str__(self) -> str:
        return f"Author: {self.author}\n Title: {self.title}\n Genre: {format_genre(self.genre)}\n Year: {self.year}\n Pages: {self.pages}\n Date of completion: {self.date_of_completion}\n"


# other functions


def format_genre(genre_set: set[str]) -> str:
    return ", ".join(sorted(genre_set))


def enter_genres(prompt="enter genres separated by commas: ") -> set[str]:
    user_input = input(prompt)
    return {item.strip() for item in user_input.split(",")}


def enter_date(prompt="enter the date in the format year/month/day") -> datetime.date:
    year = int(input("\n- enter a year: "))
    month = int(input("\n- enter a month: "))

    if month < 0 or month > 12:
        raise ValueError("month should be an integer from 1 to 12!")

    day = int(input("\n- enter a day: "))
    if day < 0 or day > 30:
        raise ValueError("day should be a positive integer from 1 to 31!")

    return datetime.date(year, month, day)
