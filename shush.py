import librosa
import soundfile as sf
import numpy as np
from scipy.signal import butter, filtfilt

def bandpass_filter(data, lowcut, highcut, fs, order=5):
    """Apply a bandpass filter to isolate specific frequency ranges."""
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    y = filtfilt(b, a, data)
    return y

def reduce_rain_noise(input_audio_file, output_audio_file):
    # Load the audio file
    y, sr = librosa.load(input_audio_file, sr=None)

    # Apply a bandpass filter to isolate the music range
    music_audio = bandpass_filter(y, 100, 2700, sr)

    # Save the filtered audio
    sf.write(output_audio_file, music_audio, sr)

# Define input and output files
input_audio = "os_noisy.wav"
output_audio = "os_clean.wav"

# Call the function
reduce_rain_noise(input_audio, output_audio)
