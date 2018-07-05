import librosa
import numpy as np
import IPython.display
import librosa.display
import matplotlib.style as ms
import matplotlib.pyplot as plt
ms.use('seaborn-muted')

audio_path = 'mp3/Bolero.mp3'

music, fs = librosa.load(audio_path)
S = librosa.feature.melspectrogram(music, sr=fs, n_mels=128)
dB = librosa.logamplitude(S, ref_power=np.max)

harmonic, percussive = librosa.effects.hpss(music)
Spectrogram_harmonic = librosa.feature.melspectrogram(harmonic, sr=fs)
Spectrogram_percussive = librosa.feature.melspectrogram(percussive,sr=fs)

dB_harmonic = librosa.logamplitude(Spectrogram_harmonic, ref_power=np.max)
dB_percussive = librosa.logamplitude(Spectrogram_percussive, ref_power=np.max)

plt.figure(figsize=(12,6))

plt.subplot(2,1,1)
librosa.display.specshow(dB_harmonic, sr=fs, y_axis='mel')
plt.title('mel power spectrogram(Harmonic)')
plt.colorbar(format='%+02.0f dB')

plt.subplot(2,1,2,)
librosa.display.specshow(dB_percussive, sr=fs, x_axis='time', y_axis='mel')
plt.title('mel power spectrogram(Percussive)')
plt.colorbar(format='+02.0f dB')

#plt.show()

