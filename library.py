"""
Сделать функцию show_book(), она показывает одну книгу
Доделать выборы в меню
Если функция поиска ничего не нашла, она должна об этом сказать 
Очистка экрана
"""


import sys


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


def show_options(options: list) -> None:
    for num, option in enumerate(options):
        print(f"{num}. {option}")


def close_library() -> None:
    """Закрывает программу"""
    print("Вы вышли из библтотеки! Приходите к нам ещё!")
    sys.exit()


def visit_menu() -> None:
    while True:
        options = [
            ("Показать все кники, которые есть в библиотеке", lambda: show_books()),
            ("Добавить книгу в библиотеку", lambda: add_book()),
            ("Удалить книгу из библиотеки", lambda: remove_book()),
            ("Найти книгу по порядковому номеру", lambda: search_by_numder()),
            ("Найти книгу по названию", lambda: search_book_by_key('название')),
            ("Найти книгу по автору", lambda: search_book_by_key('автор')),
            ("Найти книгу по году", lambda: search_book_by_key('год')),
            ("Выйти из библиотеки", lambda: close_library()),
        ]

        # 1. Показать все кники, которые есть в библиотеке
        
        for i, option in enumerate(options, start=1):
            print(i, option[0])

        option_num = input("Введите номер варианта и нажмите ENTER: ")
        idx = int(option_num) - 1
        options[idx][1]()
    


def show_books() -> None:
    """выводит на экран все книги"""
    if not library:
        print("Библиотека пуста")
        return

    for num, book in enumerate(library, 1):
        print("номер на полке", num)
        print("название", book["название"])
        print("автор", book["автор"])
        print("год", book["год"])
        print("")
    input("Нажмите ENTER чтобы продолжить")
    print("")
    return visit_menu()


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
    input("Нажмите ENTER чтобы продолжить")
    print("")
    return visit_menu()


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
    input("Нажмите ENTER чтобы продолжить")
    print("")
    return visit_menu()


def search_by_numder() -> None:
    """Выводит на экран книгу, если она нашлась по порядковому номеру"""
    if not library:
        print("Библиотека пуста!")
        return

    num = input("введите порядковый номер книги для поиска: ")

    if num.isdigit():
       num = int(num)
    else:
        print("Номер должен быть числом больше нуля!")
        return

    idx = num - 1

    if idx < 0 or idx >= len(library):
        print("Нет книги с таким номером!")
        return

    book = library[idx]

    print("Книга найдена :)")
    print("номер на полке", num)
    print("название", book["название"])
    print("автор", book["автор"])
    print("год", book["год"])
    print("")
    input("Нажмите ENTER чтобы продолжить")
    print("")
    return visit_menu()


# по названию
def search_book_by_key(user_key: str) -> None:
    """Показывает на экране книгу по ключу, если он есть"""
    
    if not library:
        print("Библиотека пуста!")
        return

    user_value = input(f"Введите {user_key}: ")

    if not user_value:
        print("Нет данных для поиска!")
        return

    if user_key == "год":
        if user_value.isdigit():
            user_value = int(user_value)

    for book in library:
        if book[user_key] == user_value:
            print("")
            print(f"Книга найдена :)")
            print(f"номер на полке: {library.index(book) + 1}")
            print(f"название: {book['название']}")
            print(f"автор: {book['автор']}")
            print(f"год: {book['год']}")
            print("")
    input("Нажмите ENTER чтобы продолжить")
    print("")
    return visit_menu()

    
# тестирование
visit_menu()