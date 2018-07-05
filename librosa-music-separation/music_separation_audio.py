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

percussive = librosa.effects.percussive(music, margin=3.0)
harmonic = librosa.effects.harmonic(music, margin=3.0)

librosa.output.write_wav("percussive.wav", percussive, fs)
librosa.output.write_wav("harmonic.wav", harmonic, fs)


