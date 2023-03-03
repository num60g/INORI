import numpy as np
import matplotlib.pyplot as plt

def generate_waveform(freq, sample_rate, duration):
    """Generates a sine wave of the given frequency, sample rate, and duration."""
    # Calculate the number of samples
    num_samples = int(sample_rate * duration)

    # Calculate the time for each sample
    times = np.arange(num_samples) / float(sample_rate)

    # Generate the sine wave
    waveform = np.sin(2.0 * np.pi * freq * times)

    return waveform, times

def generate_light_tower():
    """Generates the parameters of a light tower, including its position, radius, height, and color."""
    # Generate the position of the light tower as a random point on a 2D plane
    position = np.random.uniform(-10, 10, size=2)

    # Generate the radius of the light tower as a random value between 1 and 5
    radius = np.random.uniform(1, 5)

    # Generate the height of the light tower as a random value between 1 and 10
    height = np.random.uniform(1, 10)

    # Generate the color of the light tower as a random RGBA value
    color = np.random.uniform(0, 1, size=4)

    return position, radius, height, color

# Set the sample rate and duration of the audio file to be generated
sampling_freq = 44100
duration = 5

# Generate a time axis for the audio file
time_axis = np.linspace(0, duration, sampling_freq * duration)

# Generate a frequency axis for the audio file
freq_axis = np.fft.fftfreq(sampling_freq * duration, d=1.0 / sampling_freq)

# Generate random values for the magic power and magic skill of the user
magic_power = np.random.uniform(0, 1)
magic_skill = np.random.uniform(0, 1)

# Generate an audio waveform as a combination of two sine waves
waveform = np.sin(2 * np.pi * magic_power * 1000 * time_axis) \
           + np.sin(2 * np.pi * (magic_power + magic_skill) * 5000 * time_axis)

# Generate a waveform of a 440 Hz sine wave
freq = 440.0
waveform, times = generate_waveform(freq, sampling_freq, duration)

# Take the Fourier transform of the waveform to get its frequency spectrum
freq_spectrum = np.abs(np.fft.fft(waveform))

# Generate the parameters of a light tower
position, radius, height, color = generate_light_tower()

# Plot the waveform and frequency spectrum
plt.subplot(211)
plt.plot(times, waveform)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(212)
plt.plot(freq_axis, freq_spectrum)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')

# Draw a circle to represent the light tower's area of effect
circle = plt.Circle(position, radius, color=color, alpha=0.5)
plt.gca().add_artist(circle)

# Draw a line to represent the light tower's height
plt.plot([

