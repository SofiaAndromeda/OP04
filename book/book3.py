import csv

file_name = 'books.csv'

books_list = [
      {'Название': 'Голод', 'Автор': 'Кнут Гамсун', 'Год издания': 1890},
      {'Название': 'Фиалки по средам', 'Автор': 'Андре Моруа', 'Год издания': 1953}
]

with open(file_name, 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    for item in books_list:
        writer.writerow([item['Название'], item['Автор'], item['Год издания']])

print(f'Данные успешно записаны в файл: {file_name}')