import numpy as np
import matplotlib.pyplot as plt

def generate_waveform(freq, sample_rate, duration):
    """指定された周波数、サンプルレート、時間長に基づいて正弦波を生成する"""
    # サンプル数を計算する
    num_samples = int(sample_rate * duration)

    # サンプルごとの時間を計算する
    times = np.arange(num_samples) / float(sample_rate)

    # 正弦波の波形を生成する
    waveform = np.sin(2.0 * np.pi * freq * times)

    return waveform, times

# パラメータを設定する
freq = 440.0  # 周波数
sample_rate = 44100  # サンプルレート
duration = 5.0  # 時間長

# 波形を生成する
waveform, times = generate_waveform(freq, sample_rate, duration)

# 波形をプロットする
plt.plot(times, waveform)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()
