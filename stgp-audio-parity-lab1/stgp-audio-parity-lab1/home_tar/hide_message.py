import wave
import numpy as np
from getpass import getpass

def hide_message(audio_file, message):
    with wave.open(audio_file, 'rb') as audio:
        params = audio.getparams()
        frames = audio.readframes(audio.getnframes())
    audio_data = np.frombuffer(frames, dtype=np.int16).copy()
    bits = ''.join(format(ord(c), '08b') for c in message)
    for i in range(len(bits)):
        audio_data[i] &= ~1
        audio_data[i] |= int(bits[i])
    with wave.open('output.wav', 'wb') as output:
        output.setparams(params)
        output.writeframes(audio_data.tobytes())

message = getpass("Enter the message: ") + '\0'
hide_message('input.wav', message)
print("Message hidden in output.wav")
