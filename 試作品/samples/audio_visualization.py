"""
audio_visualization.py

This script generates and displays an audio waveform and its frequency spectrum. It also plays an audio file generated using a combination of two sine waves.

Usage:
    python audio_visualization.py

Author:
    Your Name (your.email@example.com)
"""

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

def generate_waveform(freq, sample_rate, duration):
    """Generates a sine wave of the given frequency, sample rate, and duration."""
    # Calculate the number of samples
    num_samples = int(sample_rate * duration)

    # Calculate the time for each sample
    times = np.arange(num_samples) / float(sample_rate)

    # Generate the sine wave
    waveform = np.sin(2.0 * np.pi * freq * times)

    return waveform, times

# Set the sample rate and duration of the audio file to be generated
sampling_freq = 44100
duration = 5

# Generate a time axis for the audio file
time_axis = np.linspace(0, duration, sampling_freq * duration)

# Generate a frequency axis for the audio file
freq_axis = np.fft.fftfreq(sampling_freq * duration, d=1.0 / sampling_freq)

# Generate two random numbers to use as inputs for the sine waves
magic_power = np.random.uniform(0, 1)
magic_skill = np.random.uniform(0, 1)

# Generate an audio waveform as a combination of two sine waves
waveform = np.sin(2 * np.pi * magic_power * 1000 * time_axis) \
           + np.sin(2 * np.pi * (magic_power + magic_skill) * 5000 * time_axis)

# Play the audio waveform
sd.play(waveform, sampling_freq)

# Generate a waveform of a 440 Hz sine wave
freq = 440.0
waveform, times = generate_waveform(freq, sampling_freq, duration)

# Plot the waveform
plt.subplot(211)
plt.plot(times, waveform)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# Take the Fourier transform of the waveform to get its frequency spectrum
freq_spectrum = np.abs(np.fft.fft(waveform))

# Plot the frequency spectrum
plt.subplot(212)
plt.plot(freq_axis, freq_spectrum)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.show()