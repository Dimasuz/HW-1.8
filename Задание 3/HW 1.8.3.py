# В папке лежит некоторое количество файлов. Считайте, что их количество и имена вам заранее известны
# Необходимо объединить их в один по следующим правилам:
# Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них (то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
# Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем
# Пример Даны файлы: 1.txt

# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1
# 2.txt

# Строка номер 1 файла номер 2
# Итоговый файл:

# 2.txt
# 1
# Строка номер 1 файла номер 2
# 1.txt
# 2
# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1

import os

file_list = os.listdir()
print(file_list)
# file_list = ['1.txt', '2.txt', '3.txt']

new_file = []
file_text = ''

for i in file_list:
    with open(i, encoding='utf-8') as file_obj:
        lines = file_obj.readlines()
        new_file.append([i, len(lines), lines])

def sort_len(e):
    return e[1]

new_file = sorted(new_file, key=sort_len)

for i in range(len(new_file)):
    file_text += new_file[i][0] + '\n'
    file_text += str(new_file[i][1]) + '\n'
    file_text += ''.join(new_file[i][2]) + '\n'

with open('new_file.txt', 'w') as f:
    f.write(file_text)

