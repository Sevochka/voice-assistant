import random

from thefuzz import fuzz

from config import VOICE_COMMANDS, VOICE_COMMANDS_RESPONSES
from recognition import start_listener
from talk import talk
from utils.time import get_time
from utils.weather import get_weather


def get_command(command):
    rc = {'cmd': '', 'percent': 0}
    for c, v in VOICE_COMMANDS.items():
        for x in v:
            vrt = fuzz.ratio(command, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc

def get_random_element(elements):
    return random.choice(elements)

def handle_listener(command):
    print(command)
    command_obj = get_command(command)

    if command_obj['percent'] < 50:
        talk("Я вас не поняла!")
        return True

    cmd = command_obj['cmd']
    replica = get_random_element(VOICE_COMMANDS_RESPONSES[cmd])

    if cmd == 'time':
        data = get_time()
        talk(replica.format(**data))
        return True

    if cmd == 'stop':
        talk(replica)
        return False

    if cmd == 'weather':
        data = get_weather()
        talk(replica.format(**data))
        return True

    talk(replica)
    return True


def start():
    talk("Я вас слушаю!")
    start_listener(handle_listener)


start()