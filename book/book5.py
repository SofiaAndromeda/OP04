import csv

file_name = 'books.csv'

title = input("Введите название книги: ")
name = input("Введите имя и фамилию автора: ")
age = input("Введите год издания: ")

with open(file_name, 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([title, name, age])

print(f'Книга {title}, успешно добавлена в файл: {file_name}')