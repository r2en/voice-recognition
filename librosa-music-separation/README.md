# LibROSAを使った音源分離

ハーモニックとパーカッシブに分離させる

## 1. HarmonicとPercussiveを分離させた図

[librosa.effects.hpss(y, **kwargs)](http://librosa.github.io/librosa/generated/librosa.effects.hpss.html?highlight=hpss#librosa.effects.hpss)でnumpy形式で音声ファイルをharmonicとpercussiveに分離させる。

harmonicとpercussiveの意味はよくわからなかったが聞いてみた感想としてはharmonicが弦楽器とアカペラが抽出されていて、percussiveは打楽器とアカペラが抽出されていた。

そのあとは、前の記事のスペクトログラムのプロットと同様の手順を踏んでいる。

### 結果

![separation](https://user-images.githubusercontent.com/28590220/28965886-4eff2162-794e-11e7-894b-a7fcdf1f7c00.png)

### コード

```python
import librosa
import numpy as np
import IPython.display
import librosa.display
import matplotlib.style as ms
import matplotlib.pyplot as plt
ms.use('seaborn-muted')

audio_path = 'mp3/osomatu.mp3'

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

plt.show()

```

## 2. HarmonicとPercussiveを分離させた音声ファイル

今回の本命。[librosa.effects.harmonic](http://librosa.github.io/librosa/generated/librosa.effects.harmonic.html?highlight=librosa%20effects)(y, **kwargs)関数と[librosa.effects.percussive](http://librosa.github.io/librosa/generated/librosa.effects.percussive.html?highlight=librosa%20effects)(y, **kwargs)関数で分ける

### 結果
音声データは著作権が切れた[Bolero]()を分離させた。気になった人は僕のGithubからダウンロードしてください。できればここに貼り付けたいけれども方法がわからないのでわかる人はぜひ教えてください。

### コード
```python
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
```
