"""
Напишите программу создающую еще 1 .txt файл и запишите туда строку "но у меня не получается".
Создайте еще 1 .txt файл в котором будет объединение этого файла с файлом с предыдущего задания.
"""
with open('text.txt', 'a') as file:
    file.write(' Но у меня не получается')

with open('text.txt', 'r') as file_1:
    read = file_1.read()
print(read)