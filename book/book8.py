import csv

file_name = 'books.csv'

with open(file_name, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    next(reader, None)

    for item in reader:
        print(item[0], item[1], item[-1])

    remove = input("Введите название книги, котрую хотите удалить: ")

    remove_books = [item for item in reader if item[0] != remove]

    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        fieldnames = ['Название', 'Автор', 'Год издания']
        writer.writerow(fieldnames)
        writer.writerows(remove_books)
print(f'Книга {remove} успешно удалена из файла: {file_name}')
