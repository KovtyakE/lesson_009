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
    def __init__(self, input_file, output_file):
        self.log_file = input_file
        self.output_file = output_file

    def open_and_compare(self, value_to_compare):
        output_file_create = open(file=self.output_file, mode='w', encoding='cp1251')
        output_file_create.close()
        with open(file=test.log_file, mode='r', encoding='cp1251') as logfile:
            if value_to_compare == 'minutes':
                group.compare_lines(file=logfile)
            elif value_to_compare == 'hours':
                group_hour.group_by_hours(file=logfile)
            elif value_to_compare == 'days':
                group_day.group_by_days(file=logfile)
            elif value_to_compare == 'months':
                group_month.group_by_months(file=logfile)
            elif value_to_compare == 'years':
                group_year.group_by_years(file=logfile)
            else:
                print('Wrong value to compare')

    def write_in_file(self, line, stop, count):
        line_to_write = line[:stop] + line[27]  # all symbols before ":stop sign" + symbol ']'
        with open(file=self.output_file, mode='a', encoding='cp1251') as output_file:
            output_file.write(line_to_write)
            output_file.write(' ')
            output_file.write(str(count))
            output_file.write('\n')


class GroupEvents:
    def __init__(self):
        self.stop = 17  # first 17 symbols, '[yyyy-mm-dd hh:mm'
        self.count = 0
        self.prev_line = ''

    def compare_lines(self, file):
        for line in file:
            if 'NOK' in line:
                if line[:self.stop] == self.prev_line[:self.stop]:
                    self.count += 1
                else:
                    if self.prev_line != '':
                        test.write_in_file(line=self.prev_line, stop=self.stop, count=self.count)
                    self.count = 1
                    self.prev_line = line
        test.write_in_file(line=self.prev_line, stop=self.stop, count=self.count)


# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

class GroupByHours(GroupEvents):
    def group_by_hours(self, file):
        self.stop = 14  # first 14 symbols, '[yyyy-mm-dd hh'
        self.compare_lines(file=file)


class GroupByDays(GroupEvents):
    def group_by_days(self, file):
        self.stop = 11  # first 11 symbols, '[yyyy-mm-dd'
        self.compare_lines(file=file)


class GroupByMonths(GroupEvents):
    def group_by_months(self, file):
        self.stop = 8  # first 8 symbols, '[yyyy-mm'
        self.compare_lines(file=file)


class GroupByYears(GroupEvents):
    def group_by_years(self, file):
        self.stop = 5  # first 5 symbols, '[yyyy'
        self.compare_lines(file=file)


group = GroupEvents()
group_hour = GroupByHours()
group_day = GroupByDays()
group_month = GroupByMonths()
group_year = GroupByYears()
test = LogParser(input_file='events.txt', output_file='output.txt')
test.open_and_compare(value_to_compare='months')  # can be 'minutes', 'hours', 'days', 'months', 'years'.
