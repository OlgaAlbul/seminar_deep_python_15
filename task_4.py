# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.
import argparse
import datetime

DAYS = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
parser = argparse.ArgumentParser(description='Find date')
parser.add_argument('-date', metavar='date', type=str, nargs='*', help='Enter a number of weekday in month')
parser.add_argument('-day', metavar='day', type=int, default=datetime.datetime.now().weekday(), help='Enter a number of weekday in month')
parser.add_argument('-dow', metavar='dow', type=str, default=DAYS[datetime.datetime.now().weekday()], help='Enter a name of weekday')
parser.add_argument('-mon', metavar='mon', type=str, default=datetime.datetime.now().month, help='Enter a month name')
args = parser.parse_args()


def _is_leap_year(year):
    return bool(not year % 4 and year % 100 or not year % 400)


def convert_string_to_date(day_number, day_name, month_name):
    current_year = datetime.datetime.now().year

    weekday_names = ['понедельник', 'вторник', 'среда', 'четверг',
                     'пятница', 'суббота', 'воскресенье']
    month_names = {
        'янв': (31, 1), 'фев': (29 if _is_leap_year(current_year) else 28, 2),
        'мар': (31, 3), 'апр': (30, 4), 'май': (31, 5), 'июн': (30, 6),
        'июл': (31, 7), 'авг': (31, 8), 'сен': (30, 9),
        'окт': (31, 10), 'ноя': (30, 11), 'дек': (31, 12)}
    try:
        # parts = text.split()
        # day_number = int(''.join([i for i in parts[0] if i.isdigit()]))
        # day_name = parts[1]
        # month_name = parts[2]

        first_day = datetime.datetime.strptime(f'1 {month_name} {current_year}',
                                               "%d %m %Y").weekday()
    except:
        raise ValueError
    count = 0
    weekday_names = weekday_names[first_day:] + weekday_names[:first_day]

    while count < month_names[month_name[:3]][0]:
        if day_name == weekday_names[count % 7]:
            day_number -= 1
            if not day_number:
                break
        count += 1
    else:
        raise ValueError

    return count + 1


convert_string_to_date(args.day, args.dow, args.mon)