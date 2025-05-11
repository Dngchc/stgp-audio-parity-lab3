import wave
import numpy as np

def decode_message_from_wav(wav_file, message_length):
    with wave.open(wav_file, 'rb') as wav:
        n_frames = wav.getnframes()
        frames = wav.readframes(n_frames)
        audio_data = np.frombuffer(frames, dtype=np.int16)

        decoded_message_bits = []
        bit_length = message_length * 8

        for i in range(0, bit_length, 8):
            byte = 0
            for j in range(8):
                byte |= (audio_data[i + j] & 1) << (7 - j)
            decoded_message_bits.append(byte)

        #decoded_message = bytes(decoded_message_bits)
        #Sinh vien can doc hieu code va sua lai de code hoat dong dung
        try:
            decoded_message_str = decoded_message.decode('utf-8')
        except UnicodeDecodeError:
            decoded_message_str = "Invalid message (cannot decode as ASCII)"

        return decoded_message_str

wav_file = 'output.wav'
decoded_message = decode_message_from_wav(wav_file, 8)

print(f"Decoded message: {decoded_message}")

