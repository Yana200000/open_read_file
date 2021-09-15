import os
from typing import Dict, Tuple, List

file1 = open("1.txt", "w")
file1.write("""Начальник  полиции
лично позвонил в шестнадцатый участок. А спустя  одну минуту тридцать секунд
в дежурке и других комнатах нижнего этажа раздались звонки
     Когда Иенсен  --  комиссар  шестнадцатого  участка --  вышел  из своего
кабинета,  звонки еще  не смолкли. Иенсен был мужчина средних лет,  обычного
сложения, с лицом плоским и невыразительным. На последней ступеньке винтовой
лестницы  он задержался  и  обвел взглядом помещение дежурки. Затем поправил
галстук и проследовал к машине.""")
file1.close()

file2 = open("2.txt", "w")
file2.write("""Тревога началась в тринадцать часов ноль две минуты. """)
file2.close()

file3 = open("3.txt", "w")
file3.write("""В  это время  дня  машины текли сплошным  блестящим  потоком,  а  среди
потока, будто  колонны из бетона  и стекла, высились  здания. Здесь,  в мире
резких граней,  люди  на тротуарах  выглядели  несчастными и  неприкаянными.
Одеты они были хорошо, но как-то удивительно походили друг на друга и все до
одного спешили. Они шли нестройными  вереницами, широко разливались, завидев
красный  светофор или  металлический  блеск кафе-автоматов.  Они непрестанно
озирались по сторонам и теребили портфели и сумочки.
     Полицейские  машины  с  включенными  сиренами  пробивались  сквозь  эту
толчею.""")
file3.close()

os.chdir(r'C:\Users\User\Desktop\Нетология\hw 12.09')

def merging_files():
    list_files_txt =[]
    my_dict = {}
    for files in os.listdir(r"C:\Users\User\Desktop\Нетология\hw 12.09"):
        if files.endswith(".txt"):
            list_files_txt.append(files)
            for i in list_files_txt[::-1]:
                with open(i, encoding='cp1251') as files:
                    list_strings = files.readlines()
                    my_dict[i] = (len(list_strings), list_strings)
    sort_dict ={}
    list_for_sort = list(my_dict.items())
    list_for_sort.sort(key=lambda i: i[1])
    for i in list_for_sort:
        sort_dict[i[0]] = i[1]

    with open("file4.txt", "w", encoding='cp1251') as fail:
        for key, value in sort_dict.items():
            fail.write(f'{key}\n{value[0]}\n{"".join(value[1])}\n')



print(merging_files())
