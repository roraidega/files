"""
Разработайте программу, которая будет показывать слово (или слова),
чаще остальных встречающееся в текстовом файле(файл для проверки можно ручками создать). Сначала пользователь
должен ввести имя файла для обработки. После этого вы должны открыть
файл и  проанализировать его построчно, разделив при этом строки по
словам и исключив из них пробелы и знаки препинания. Также при подсчете частоты появления слов в файле вам стоит игнорировать регистры
"""
Froz = {}
with open('text.txt', 'r+') as file_1:
    for line in file_1.readlines():
        for sym in line.lower().split():
            for rep in sym:
                if rep in ',/.-!@#$%^&+)(*&}{][':
                    sym = sym.replace(rep, '')
            Froz[sym] = 0
    file_1.seek(0)
    for line_2 in file_1.readlines():
        for sym in line_2.lower().split():
            for rep in sym:
                if rep in ',/.-!@#$%^&+)(*&}{][':
                    sym = sym.replace(rep, '')
            Froz[sym] += 1

Froz = sorted(Froz, key=lambda x: Froz[x])

print(Froz[0])










