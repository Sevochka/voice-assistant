from datetime import datetime
from num2words import num2words


def get_time():
    now = datetime.now()
    seconds = num2words(now.strftime("%S"), lang='ru')
    minutes = num2words(now.strftime("%M"), lang='ru')
    hours = num2words(now.strftime("%H"), lang='ru')

    return {"time": f"{hours} часов {minutes} минут {seconds} секунд"}
