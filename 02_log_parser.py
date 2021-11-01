# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class LogParser:
    def __init__(self, filename):
        self.log_file = filename
        self.output_file = 'output.txt'

    def write_stat_in_file(self):
        output_file_create = open(file=self.output_file, mode='w', encoding='cp1251')
        output_file_create.close()

        with open(file=self.log_file, mode='r', encoding='cp1251') as file:
            prev_line = 0
            for line in file:
                if 'NOK' in line:
                    # TODO
                    #  group.somefunc which compares prev and current lines[:some val for templates, ---
                    #  ---standard :17] and counting it
                    #  somefunc which cuts our string after comparing
                    #  somefunc for write in file
                    self.count = 0
                    self.current_line = line[:17] + line[27]  # all symbols before ":seconds" + symbol ']'
                    if self.current_line == prev_line:
                        continue
                    prev_line = self.current_line
                    group.compare_lines()
                    with open(file=self.output_file, mode='a', encoding='cp1251') as output_file:
                        output_file.write(self.current_line)
                        output_file.write(' ')
                        output_file.write(str(self.count))
                        output_file.write('\n')

                    # преобразовать в читабельный вид строку
                    # проверить наличие такой строки в файле, если есть:
                    #     изменить число после выведенной строки на каунт+1
                    # если нет:
                    #     добавить строку в файл с цифрой 1


class GroupEvents:
    def compare_lines(self, start=1, stop=17):  # full compare (yyyy-mm-dd hh:mm)
        with open(file=test.log_file, mode='r', encoding='cp1251') as file:
            for line in file:  # lines from another class (test)
                if 'NOK' in line:
                    if test.current_line[start:stop] == line[start:stop]:
                        test.count += 1


group = GroupEvents()
test = LogParser(filename='events.txt')
test.write_stat_in_file()

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
