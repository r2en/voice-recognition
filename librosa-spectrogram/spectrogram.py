import librosa
import numpy as np
import IPython.display
import librosa.display
import matplotlib.style as ms
import matplotlib.pyplot as plt
ms.use('seaborn-muted')

audio_path = 'mp3/fortune.mp3'

y, sr = librosa.load(audio_path)
S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)

dB = librosa.logamplitude(S, ref_power=np.max)

plt.figure(figsize=(12,4))

librosa.display.specshow(dB, sr=sr, x_axis='time', y_axis='mel')
plt.title('Mel Power Spectrogram')
plt.colorbar(format='%+0.20f dB')
plt.show()