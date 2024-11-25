# library_ms (Консольная система управления библиотекой.)

# Тестовое задание 
Задание: Разработка системы управления библиотекой
- Описание
  - Необходимо разработать консольное приложение для управления библиотекой книг.
  Приложение должно позволять добавлять, удалять, искать и отображать книги.
  Каждая книга должна содержать следующие поля:
    -  id (уникальный идентификатор, генерируется автоматически)
    - title (название книги)
    - author (автор книги)
    - year (год издания)
    - status (статус книги: “в наличии”, “выдана”)

## Требования
1. Добавление книги: Пользователь вводит title, author и year, после чего книга добавляется в библиотеку с уникальным id и статусом “в наличии”.
2. Удаление книги: Пользователь вводит id книги, которую нужно удалить.
3. Поиск книги: Пользователь может искать книги по title, author или year.
4. Отображение всех книг: Приложение выводит список всех книг с их id, title, author, year и status.
5. Изменение статуса книги: Пользователь вводит id книги и новый статус (“в наличии” или “выдана”).

## Дополнительные требования
 - Реализовать хранение данных в текстовом или json формате.
 - Обеспечить корректную обработку ошибок (например, попытка удалить несуществующую книгу).
 - Написать функции для каждой операции (добавление, удаление, поиск, отображение, изменение статуса).
 - Не использовать сторонние библиотеки.

## Критерии оценки:
 • Корректность и полнота реализации функционала.<br/>
 • Чистота и читаемость кода.<br/>
 • Обработка ошибок и исключений.<br/>
 • Удобство использования интерфейса командной строки.<br/>
 • Структура проекта.

## Будет плюсом:
1. Аннотации: Аннотирование функций и переменных в коде.
2. Документация: Наличие документации к функциям и основным блокам кода.
3. Описание функционала: Подробное описание функционала приложения в README файле.
4. Тестирование.
5. Объектно-ориентированный подход программирования.

---
# Описание работы программы:
Для хранения данных о книгах используем JSON-файл (```library.json```), создаётся при сохранении книги.<br/>
Для добавления книги надо указать: название книги, автора книги и год издания.<br/>

Меню: Пользователь может выбирать цифрами, что ему нужно сделать (добавить книгу, удалить, поиск, отображение списка всех книг, изменение статуса и выход из программы).<br/>

Функции:
1. add_book(): Добавляет книгу в библиотеку.
2. remove_book(): Удаляет книгу по ID.
3. search_books(): Ищет книги по названию, автору или году.
4. display_books(): Отображает все книги.
5. change_status(): Изменяет статус книги.
6. завершает работу программы
