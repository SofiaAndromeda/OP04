import csv as knishka

new_file_name = input('Введите имя нового файла: ')

with open(new_file_name, 'w', newline='', encoding='utf-8') as file:
    books_data = [
        {'Название': 'О чём я говорю, когда говорю о беге', 'Автор': 'Харуки Мураками', 'Год издания': 2007},
        {'Название': 'Собор Парижской Богоматери', 'Автор': 'Виктор Гюго', 'Год издания': 1831}]
    writer = knishka.writer(file)
    for item in books_data:
        writer.writerow([item['Название'], item['Автор'], item['Год издания']])

with open(new_file_name, newline='', encoding='utf-8') as file:
    reader = knishka.reader(file)

    for item in reader:
        print(item[0], item[1], item[-1])
