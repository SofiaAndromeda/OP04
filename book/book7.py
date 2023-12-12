import csv
import shutil

orig_file = 'books.csv'
copy_file = 'books_copy.csv'

shutil.copyfile(orig_file, copy_file)

with open(copy_file, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    next(reader, None)

    for item in reader:
        print(item[0], item[1], item[-1])

print(f'Создана копия файла: {orig_file} из {copy_file}')
