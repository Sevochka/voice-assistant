import requests
from num2words import num2words

api_key = "dd6e423f7f036699ea3033727eef6c94"
base_url = "https://api.openweathermap.org/data/2.5/weather?units=metric&lang=ru&appid=" + api_key

def math_round(num):
    return round(num)

def parse_weather(weather_json):
    print(weather_json)
    if weather_json["cod"] != "404":
        main = weather_json["main"]
        return {
            "temp": num2words(round(main["temp"]), lang='ru'),
            "pressure": num2words(round(main["pressure"]), lang='ru'),
            "humidity": num2words(round(main["humidity"]), lang='ru'),
            "description": weather_json["weather"][0]["description"],
            "city": weather_json["name"]
        }

    return None


def get_weather(city_name="Moscow"):
    complete_url = base_url + "&q=" + city_name
    response = requests.get(complete_url)
    weather = parse_weather(response.json())
    return weather

exported_functions = [get_weather]