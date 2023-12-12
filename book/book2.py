import csv

file_name = 'books.csv'

with open(file_name, newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['Название'], row['Автор'], row['Год издания'])
