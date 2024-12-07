# Audio Noise Reduction for Rain

This project provides a Python script to reduce background rain noise from an audio file while preserving the music at its original volume level. The solution uses a bandpass filter to isolate and maintain music frequencies, suppressing rain noise outside this range.

## Prerequisites

Ensure you have Python 3.7+ installed. You will also need to install the following Python libraries:

- `librosa`: For audio file loading and processing.
- `soundfile`: For saving processed audio.
- `scipy`: For signal processing, including bandpass filtering.

You can install these libraries using `pip`:

```bash
pip install librosa soundfile scipy
```

Ensure that both the code file and audio file are in the same directory and your terminal as well.

### To run the code, make sure to edit it based on your audio file name.

In your terminal, run the following code:

```bash
python shush.py
```
