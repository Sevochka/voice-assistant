import json

import vosk
import sys
import sounddevice as sd
import queue
from thefuzz import fuzz

from config import VOICE_COMMANDS

model = vosk.Model("model-small")
sample_rate = 16000
device = 0

q = queue.Queue()


def queue_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def start_listener(callback):
    with sd.InputStream(samplerate=sample_rate,
                        blocksize=8000,
                        device=device,
                        dtype='int16',
                        channels=1,
                        callback=queue_callback):
        rec = vosk.KaldiRecognizer(model, sample_rate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                text = json.loads(rec.Result())["text"]
                if text == "":
                    continue
                is_continue = callback(text)
                if not is_continue:
                    break
