"""
Напишите программу создающую .txt файл и записывающую туда строку "Я гений и стараюсь учить питон".
Выведите первые 7 символов файла на экран.
"""
file = open("text.txt", "w")
file.write("Я гений и стараюсь учить питон")
file.close()
with open("text.txt", "r") as file:
    for line in file:
        print(line)