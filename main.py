"""
Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
- имя файла без расширения или название каталога,
- расширение, если это файл,
- флаг каталога,
- название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя
логирование.
"""

import os
import argparse
import logging
from collections import namedtuple

LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

logging.basicConfig(filename='log.log', level=logging.INFO, encoding='utf-8',
                    format=LOG_FORMAT)

parser = argparse.ArgumentParser(description='Get data about catalog')
parser.add_argument('-d', '--dir', metavar='path', type=str, help='directory path', default='.',
                    required=True)
args = parser.parse_args()

print(args.dir)
print(args)

DirectoryData = namedtuple('DirectoryData', ['name', 'ext', 'dir_flag', 'parent_dir'])


def get_directory_info(path):

    for dir_path, dirs, files in os.walk(path):
        for dir_name in dirs:
            dir_info = DirectoryData(name=dir_name, ext=None, dir_flag=True, parent_dir=os.path.basename(dir_path))
            logging.info(dir_info)

        for file_name in files:
            name, ext = os.path.splitext(file_name)
            file_info = DirectoryData(name=name, ext=ext, dir_flag=False, parent_dir=os.path.basename(dir_path))
            logging.info(file_info)


get_directory_info(os.path.abspath(args.dir))
