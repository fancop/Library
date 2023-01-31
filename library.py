library = [
    {
    "название": "Введение в Python. Том 1",
    "автор": "Марк Лутц",
    "год": 2022
    },
    {
    "название": "Введение в Python. Том 2",
    "автор": "Марк Лутц",
    "год": 2023
    }

]


def show_all_books() -> None:
    """ выводит на жкран все книги"""
    if not library:
        print("Библиотека пуста")
        return

    for num, book in enumerate(library, 1):
        print("номер на полке", num)
        print("название", book["название"])
        print("автор", book["автор"])
        print("год", book["год"])
        print("")


def add_book():
    """
    Добавляет в библиотеку уникальную книгу,
    если указаны автор и год.
    """
    title = input("Введите название книги:")
    if not title:
        print("Нет названия!")
        return
    author = input("Введите имя автора:")
    if not author:
        print("Нет автора!")
        return
    year = input("Введите год издания:")
    if year.isdigit():
        year = int(year)
    else:
        print("Год должен быть целым числом!")
        return

    book = {
    "название": title,
    "автор": author,
    "год": year,
    }
    if book in library:
        print("")
        print("такая книга уже есть!")
        print("")
        return


    library.append(book)
    print(f"Книга {book['название']} добавлена")


def remove_book() -> None:
    """Удаляет книгу по номеру"""

    if not library:
        print("Библиотека пуста")
        return

    num = input("введите порядковый номер книги для удаления")

    if num.isdigit():
       num = int(num)
    else:
        print("Номер должен быть числом больше нуля")
        return

    idx = num - 1

    if idx < 0 or idx >= len(library):
        print("Нет книги с таким номером")
        return

    print(f"Книга {library[idx]['название']} удалена")
    library.pop(idx)


def search_by_numder() -> None:
    """Выводит на экран книгу, если она нашлась по порядковому номеру"""
    if not library:
        print("Библиотека пуста")
        return

    num = input("введите порядковый номер книги для поиска")

    if num.isdigit():
       num = int(num)
    else:
        print("Номер должен быть числом больше нуля")
        return

    idx = num - 1

    if idx < 0 or idx >= len(library):
        print("Нет книги с таким номером")
        return

    print(f"Книга {library[idx]['название']} найдена")



show_all_books()
print("------------------------------------------------")
search_by_numder()
print("------------------------------------------------")
show_all_books()