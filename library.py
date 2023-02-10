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


def visit_menu() -> None:
    text = "Библиотека деревни «Гадюкино»: "
    options = [
        "Показать все кники, которые есть в библиотеке",
        "Добавить книгу в библиотеку",
        "Удалить книгу из библиотеки",
        "Найти книгу по порядковому номеру",
        "Найти книгу по названию",
        "Найти книгу по автору",
        "Найти книгу по году", 
        "Выйти из библиотеки",
    ]
    print(text)
    show_options(options)
    option = input("Введите номер варианта и нажмите ENTER: ")
    if option == "0":
        return show_books()
    elif option == "1":
        return add_book()
    elif option == "2":
        return remove_book()
    elif option == "3":
        return search_by_numder()
    elif option == "4":
        return search_book_by_key('Название')
    elif option == "5":
        return search_book_by_key('автор')
    elif option == "6":
        return search_book_by_key('год')
    elif option == "7":
        print("Приходите к нам ещё! Тут будет ещё больше разных книг!")
        exit
    else:
        print("Такой вариант еще не сделан :(")
        return visit_menu()


def show_books() -> None:
    """ выводит на экран все книги"""
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
