import datetime

def datetime_used():  # Повертає поточну дату і час у форматі "день.місяць.рік години:хвилини"
    return datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
