import vosk
import sys
import sounddevice as sd
import queue

model = vosk.Model("model")
sample_rate = 16000
device = 1

q = queue.Queue()


def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


with sd.InputStream(samplerate=sample_rate,
                    blocksize=8000,
                    device=device,
                    dtype='int16',
                    channels=1,
                    callback=callback):
    rec = vosk.KaldiRecognizer(model, sample_rate)
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            print(rec.Result())
        else:
            print(rec.PartialResult())


