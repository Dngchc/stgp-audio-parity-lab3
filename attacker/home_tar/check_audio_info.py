import os
import wave
import audioop

def check_audio_properties(file_path):
    """
    Checks basic properties of a WAV audio file.

    Args:
        file_path (str): The path to the WAV audio file.

    Returns:
        dict: A dictionary containing the file properties if it's a valid WAV file,
              otherwise returns None and prints an error message.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found at path '{file_path}'")
        return None

    try:
        with wave.open(file_path, 'rb') as wf:
            properties = {
                "Number of channels": wf.getnchannels(),
                "Sample rate": wf.getframerate(),
                "Sample width": wf.getsampwidth(),
                "Number of frames": wf.getnframes(),
                "Duration (seconds)": wf.getnframes() / wf.getframerate(),
                "Compression type": wf.getcomptype(),
                "Compression name": wf.getcompname()
            }
            return properties
    except wave.Error:
        print(f"Error: File '{file_path}' is not a valid WAV file.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    file_path = input("Enter the path to the audio file: ")
    audio_info = check_audio_properties(file_path)

    if audio_info:
        print("\nAudio file properties:")
        for key, value in audio_info.items():
            print(f"- {key}: {value}")
