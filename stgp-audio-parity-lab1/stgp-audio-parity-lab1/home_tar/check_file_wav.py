import wave
import numpy as np

def compare_similarity(file1, file2, threshold=0.99):
    with wave.open(file1, 'rb') as audio1, wave.open(file2, 'rb') as audio2:
        if audio1.getnchannels() != audio2.getnchannels():
            print("Different number of channels.")
            return False
        if audio1.getsampwidth() != audio2.getsampwidth():
            print("Different sample widths.")
            return False
        if audio1.getframerate() != audio2.getframerate():
            print("Different sample rates.")
            return False
        if audio1.getnframes() != audio2.getnframes():
            print("Different number of frames.")
            return False

        frames1 = audio1.readframes(audio1.getnframes())
        frames2 = audio2.readframes(audio2.getnframes())

        audio_data1 = np.frombuffer(frames1, dtype=np.int16)
        audio_data2 = np.frombuffer(frames2, dtype=np.int16)

        min_len = min(len(audio_data1), len(audio_data2))
        equal_samples = np.sum(audio_data1[:min_len] == audio_data2[:min_len])
        similarity = equal_samples / min_len

        print(f"Similarity: {similarity * 100:.2f}%")

        if similarity >= threshold:
            print("Files are similar enough! (Compatibility OK)")
            return True
        else:
            print("Files differ significantly.")
            return False

input_file = input("Enter the path for the original audio file (input): ")
output_file = input("Enter the path for the output audio file (after message embedding): ")

compare_similarity(input_file, output_file)

