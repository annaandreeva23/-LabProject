'''
Лаба 4 Скачати довільних не встроєних 10 бібліотек та 5 встроєних.
Використати довільний функціонал цих бібліотек.
Розділити точку входу та кожну створену функцію на різні файли.
Результат це папка в вашому репозиторію з всіма файлами їх повинно бути 16 створити фріз вашого проекту.
Остання дата закидання на гітхаб 16 жовтня включно
'''

from builtin_libs.math_used import math_used
from builtin_libs.random_used import random_used
from builtin_libs.datetime_used import datetime_used
from builtin_libs.os_used import os_used
from builtin_libs.json_used import json_used

from external_libs.numpy_used import numpy_used
from external_libs.pandas_used import pandas_used
from external_libs.faker_used import faker_used
from external_libs.pyfiglet_used import pyfiglet_used
from external_libs.colorama_used import colorama_used
from external_libs.tabulate_used import tabulate_used
from external_libs.emoji_used import emoji_used
from external_libs.humanize_used import humanize_used
from external_libs.num2words_used import num2words_used
from external_libs.pytz_used import pytz_used

if __name__ == "__main__":
    print(math_used())
    print(random_used())
    print(datetime_used())
    print(os_used())
    print(json_used())

    print(numpy_used())
    print(pandas_used())
    print(faker_used())
    print(pyfiglet_used())
    print(colorama_used())
    print(tabulate_used())
    print(emoji_used())
    print(humanize_used())
    print(num2words_used())
    print(pytz_used())