import wave
import numpy as np

def extract_message(audio_file):
    with wave.open(audio_file, 'rb') as audio:
        frames = audio.readframes(audio.getnframes())
        audio_data = np.frombuffer(frames, dtype=np.int16)
        bits = [sample & 1 for sample in audio_data]
        chars = []
        for i in range(0, len(bits), 8):
            byte = bits[i:i+8]
            if len(byte) < 8:
                break
            # Thieu dong code quan trong o day: char = chr(int(''.join(map(str, byte)), 2))
            # Dong nay chuyen doi tu day bit sang ky tu
            if char == '\0':
                break
            chars.append(char)
        return ''.join(chars)

path = input("Enter the audio file path: ")
try:
    message = extract_message(path)
    print(f"Hidden message: {message}")
    print("Successfully")
except Exception as e:
    print(f"Error: {e}")
    print("False")
