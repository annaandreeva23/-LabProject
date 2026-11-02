import datetime
import pytz

def pytz_used():  # Повертає поточний час у Києві
    return datetime.datetime.now(pytz.timezone("Europe/Kyiv")).strftime("%H:%M")
