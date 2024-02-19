# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.

import logging

logging.basicConfig(filename='error.log', level=logging.DEBUG, encoding='utf-8')

try:
    result = 10 / 0
except ZeroDivisionError:
    logging.exception('Произошла ошибка деления на ноль')

print('Программа завершена.')
