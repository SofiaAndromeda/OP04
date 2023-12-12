import csv

file_name = 'books.csv'

target_letter = input("Введите букву: ")

with open(file_name, encoding='utf-8') as file:
    reader = csv.reader(file)

    next(reader, None)

    for item in reader:
        books_list = item[1]
        if books_list and books_list.startswith(target_letter):
            print(books_list)
