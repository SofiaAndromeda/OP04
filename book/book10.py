import csv

file_name = 'books.csv'

with open(file_name, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    next(reader, None)

    reader = list(reader)

    sorted_age = sorted(reader, key=lambda item: item[-1])

    with open('sorted_age.csv', 'w', newline='', encoding='utf-8') as new_file:
        writer = csv.writer(new_file)
        fieldnames = ['Название', 'Автор', 'Год издания']
        writer.writerow(fieldnames)
        writer.writerows(sorted_age)

print(f'Сортировка завершена.')
