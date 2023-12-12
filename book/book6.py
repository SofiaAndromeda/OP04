import csv

file_name = 'books.csv'

with open(file_name, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    next(reader, None)

    books_data = list(reader)

    for item in reversed(books_data):
        print(item[0], item[1], item[-1])

print('Данные успешно выведены в обратном порядке.')
