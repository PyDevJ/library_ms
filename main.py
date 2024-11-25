import json
import os


class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.load_data()

    def load_data(self):
        """Загружает данные из файла, если файл существует."""
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as file:
                self.books = json.load(file)
        else:
            self.books = []

    def save_data(self):
        """Сохраняет данные в файл."""
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.books, file, indent=4, ensure_ascii=False)

    def add_book(self, title, author, year):
        """Добавляет книгу в библиотеку."""
        new_id = max([book["id"] for book in self.books], default=0) + 1
        new_book = {
            "id": new_id,
            "title": title,
            "author": author,
            "year": year,
            "status": "в наличии"
        }
        self.books.append(new_book)
        self.save_data()
        print(f"Книга '{title}' успешно добавлена!")

    def remove_book(self, book_id):
        """Удаляет книгу по id."""
        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            self.save_data()
            print(f"Книга с id {book_id} удалена.")
        else:
            print("Книга с таким id не найдена.")

    def find_book_by_id(self, book_id):
        """Находит книгу по id."""
        for book in self.books:
            if book["id"] == book_id:
                return book
        return None

    def search_books(self, search_term):
        """Ищет книги по title, author или year."""
        found_books = [book for book in self.books if
                       search_term.lower() in book["title"].lower() or
                       search_term.lower() in book["author"].lower() or
                       search_term in str(book["year"])]
        if found_books:
            for book in found_books:
                print(f"id: {book['id']}, title: {book['title']}, author: {book['author']}, year: {book['year']},"
                      f"status: {book['status']}")
        else:
            print("Книги не найдены.")

    def display_books(self):
        """Отображает все книги в библиотеке."""
        if not self.books:
            print("Библиотека пуста.")
        else:
            for book in self.books:
                print(f"id: {book['id']}, title: {book['title']}, author: {book['author']}, year: {book['year']},"
                      f"status: {book['status']}")

    def change_status(self, book_id, new_status):
        """Изменяет статус книги по id."""
        book = self.find_book_by_id(book_id)
        if book:
            if new_status in ["в наличии", "выдана"]:
                book["status"] = new_status
                self.save_data()
                print(f"Статус книги с id {book_id} изменен на '{new_status}'.")
            else:
                print("Неверный статус. Используйте 'в наличии' или 'выдана'.")
        else:
            print("Книга с таким id не найдена.")


def main():
    library = Library()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите действие (1-6): ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания книги: ")
            if year.isdigit():
                library.add_book(title, author, int(year))
            else:
                print("Год издания должен быть числом.")

        elif choice == "2":
            try:
                book_id = int(input("Введите id книги для удаления: "))
                library.remove_book(book_id)
            except ValueError:
                print("Неверный ввод, id должен быть числом.")

        elif choice == "3":
            search_term = input("Введите для поиска (название, автор или год): ")
            library.search_books(search_term)

        elif choice == "4":
            library.display_books()

        elif choice == "5":
            try:
                book_id = int(input("Введите id книги для изменения статуса: "))
                new_status = input("Введите новый статус ('в наличии' или 'выдана'): ")
                library.change_status(book_id, new_status)
            except ValueError:
                print("Неверный ввод, id должен быть числом.")

        elif choice == "6":
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
