# -*- coding: utf-8 -*-

import os
import shutil
import time


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk +
#   os.path.dirname
#   os.path.join
#   os.path.normpath +
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class SortFiles:
    def __init__(self, input_folder, output_folder):
        self.folder_to_scan = os.path.normpath(input_folder)
        self.new_folder = os.path.normpath(output_folder)

    def path_walk_and_copy(self):
        self.create_dir(folder_to_create=self.new_folder)
        walk = os.walk(self.folder_to_scan)
        for address, directories, files in walk:
            for file in files:
                current_path = os.path.join(address, file)
                # gmtime format - list (year, month, day, hour, minute, sec...)
                time_when_modified = time.gmtime(os.path.getmtime(current_path))
                year_of_modify = time_when_modified[0]
                month_of_modify = time_when_modified[1]
                folder_of_year = '{}\{}'.format(self.new_folder, year_of_modify)
                if not os.path.isdir(folder_of_year):
                    self.create_dir(folder_of_year)
                folder_of_month = '{}\{}\{last:0>2}'.format(self.new_folder, year_of_modify, last=month_of_modify)
                if not os.path.isdir(folder_of_month):
                    self.create_dir(folder_of_month)
                source_file = '{}\{}'.format(address, file)
                destination_folder = folder_of_month
                self.copy_to_the_new_dir(source_file=source_file, destination_address=destination_folder)

    def create_dir(self, folder_to_create):
        if os.path.isdir(folder_to_create):
            shutil.rmtree(folder_to_create)
        os.makedirs(folder_to_create)

    def copy_to_the_new_dir(self, source_file, destination_address):
        shutil.copy2(src=source_file, dst=destination_address)


script = SortFiles(input_folder='icons',
                   output_folder='icons_by_year')
script.path_walk_and_copy()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
