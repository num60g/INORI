import numpy as np

# サンプリング周波数
sampling_freq = 44100

# 長さ（秒）
duration = 5

# 時間軸
time_axis = np.linspace(0, duration, sampling_freq * duration)

# 周波数軸
freq_axis = np.fft.fftfreq(sampling_freq * duration, d=1.0 / sampling_freq)

# 魔力量
magic_power = np.random.uniform(0, 1)

# 魔術技量
magic_skill = np.random.uniform(0, 1)

# いのりの効果をランダムに生成する
waveform = np.sin(2 * np.pi * magic_power * 1000 * time_axis) \
           + np.sin(2 * np.pi * (magic_power + magic_skill) * 5000 * time_axis)

# 音波形を再生する（必要に応じて、音声ファイルとして保存する）
import sounddevice as sd
sd.play(waveform, sampling_freq)
