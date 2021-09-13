# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код

import zipfile


class Statistics_for_file:
    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        self.sorted_stat = {}

    def unzip(self):
        zip_file = zipfile.ZipFile(self.file_name, "r")
        for filename in zip_file.namelist():
            zip_file.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(file=self.file_name, mode='r', encoding='cp1251') as file:
            for line in file:
                self.collect_from_line(line=line[:-1])

    def collect_from_line(self, line):
        for char in line:
            if char.isalpha():
                if char in self.stat:
                    self.stat[char] += 1
                else:
                    self.stat[char] = 1
            else:
                continue

    def sort_by_count(self):
        self.sorted_dict = sorted(self.stat, key=self.stat.get)
        for key in self.sorted_dict:
            self.sorted_stat[key] = self.stat[key]

    # todo
    # способ отсортировать в одном методе?
    def sort_by_count_reversed(self):
        pass

    def sort_by_name(self):
        pass

    def print_sorted_stat(self):
        print('{char:-<6}+{stat:->8}'.format(char='+', stat='+'))
        print('|{char:^5}|{stat:>7}|'.format(char='Буква', stat='Частота'))
        print('{char:-<6}+{stat:->8}'.format(char='+', stat='+'))
        for key in self.sorted_stat:
            print('|{key:^5}|{value:>7}|'.format(key=key, value=self.stat[key]))


file_stat = Statistics_for_file(file_name='python_snippets/voyna-i-mir.txt.zip')
file_stat.unzip()
file_stat.collect()
file_stat.sort_by_count()
file_stat.print_sorted_stat()


# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
