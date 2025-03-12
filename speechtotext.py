from pydub import AudioSegment
import speech_recognition as sr

# Load the M4A file
audio = AudioSegment.from_file("your_file.m4a", format="m4a")

# Export to WAV
audio.export("converted.wav", format="wav")

# Initialize recognizer
recognizer = sr.Recognizer()

# Load the WAV file
with sr.AudioFile("converted.wav") as source:
    audio_data = recognizer.record(source)

# Recognize speech using Google Web Speech API in Chinese
try:
    text = recognizer.recognize_google(audio_data, language='zh-CN')  # Specify Chinese language
    print("Transcription: ", text)
except sr.UnknownValueError:
    print("Google Web Speech API could not understand the audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Web Speech API; {e}")

