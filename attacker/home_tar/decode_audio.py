import wave
import numpy as np

def decode_message_from_wav(wav_file, message_length=8):
    with wave.open(wav_file, 'rb') as wav:
        n_frames = wav.getnframes()
        frames = wav.readframes(n_frames)
        audio_data = np.frombuffer(frames, dtype=np.int16)

        decoded_message_bits = []
        bit_length = message_length * 8

        # Duyet qua cac mau de tao chuoi bit
        # Sinh vien can sua code de code hoat dong dung
        #for i in range(0, bit_length, 8):
        #    for j in range(8):
        #        decoded_message_bits.append(str(audio_data[i + j] & 1))

        if len(decoded_message_bits) == 0:
            raise ValueError("ERROR!!!!")

        decoded_bits = ''.join(decoded_message_bits)
        return decoded_bits


wav_file = input("Path of file WAV to decode: ")
decoded_bits = decode_message_from_wav(wav_file)
print("Success!")
print(f"Decoded bits: {decoded_bits}")

