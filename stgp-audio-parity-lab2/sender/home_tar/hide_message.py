from pydub import AudioSegment
import numpy as np

def hide_message_in_audio(input_audio_path, secret_message_path, output_audio_path):
    audio = AudioSegment.from_wav(input_audio_path)
    with open(secret_message_path, 'r') as f:
        secret_message = f.read()

    audio_samples = np.array(audio.get_array_of_samples())
    bit_length = len(secret_message) * 8  

    if len(audio_samples) < bit_length:
        print("Không đủ không gian trong âm thanh để giấu thông điệp.")
        return

    bit_message = ''.join(format(ord(char), '08b') for char in secret_message)

    for i in range(bit_length):
        message_bit = int(bit_message[i])
        sample = audio_samples[i]
        if sample % 2 != message_bit:
            audio_samples[i] = sample ^ 1  

    modified_audio = audio._spawn(audio_samples.tobytes())
    modified_audio.export(output_audio_path, format="wav")
    print(f"Create OK! Message successfully hidden and saved in {output_audio_path}")

hide_message_in_audio("input.wav", "secret.txt", "output.wav")
