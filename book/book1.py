import csv

books_list = [
    {'Название': 'Платье цвета полуночи', 'Автор': 'Терри Пратчетт', 'Год издания': 2010},
    {'Название': 'О чём я говорю, когда говорю о беге', 'Автор': 'Харуки Мураками', 'Год издания': 2007},
    {'Название': 'Собор Парижской Богоматери', 'Автор': 'Виктор Гюго', 'Год издания': 1831},

]

file_name = 'books.csv'

with open(file_name, 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['Название', 'Автор', 'Год издания']
    writer = csv.DictWriter(file, fieldnames)

    writer.writeheader()
    for item in books_list:
        writer.writerow(item)

print(f'Создан новый файл: {file_name}')