# LibROSAを使ったスペクトログラム

### スペクトログラム

複合信号を窓関数に通して、周波数スペクトルで計算した結果を示すもの。三次元的(時間、周波数、信号成分の強さ)で表す。

スペクトログラムは声紋の鑑定、動物の鳴き声分析、音楽、ソナー、音声処理などにも使われる。

簡単に言ってしまえば、どの音の高さ(周波数=Hz)にどれくらいうるさい音が出てる(信号成分の強さ=dB)か？、である。

dBは、図書館の音の大きさは何dBで飛行場近くの住宅街は何dBと言うのを聞いたことはないだろうか。

![spectrogram](https://user-images.githubusercontent.com/28590220/28950187-cee3b2b4-78fc-11e7-9293-e1b0f18db0a0.png)

### 生成
横軸が時間を表し、縦軸が周波数を表す。明るさや色をあr和す部分は周波数の強さ(振幅)を表す。

スペクトログラムはSTFT(短時間フーリエ変換)で計算される方法がある。時間領域で標本化されたデータをチャンクにわけ(チャンクは一般にオーバーラップさせる)、チャンク毎にフーリエ変換を施す。チャンク毎にフーリエ変換を施した変換結果を垂直に置いて時系列に並べるとスペクトログラムになる。

スペクトログラムでは、STFTの結果を絶対値を2乗したものを使う。


$$ spectrogram(t,\omega) = |STFT(t,\omega)|^2 $$

<br>
<br>

### 検証
2016年度ヒットソングで検索かけたものを選んだ

1.はなまるぴっぴはよいこだけ

![spectrogram_of_osomatu](https://user-images.githubusercontent.com/28590220/28951178-4a58e462-7904-11e7-8a2b-f9bc7684a2c9.png)

全体的に同じ音程で続く曲なのでなんとなく予想していたが、変化が一曲通して見られない。スペクトログラムに反映されている部分に特に特徴も見られない。

2.前前前世

![zense](https://user-images.githubusercontent.com/28590220/28951296-ff1be188-7904-11e7-8206-41531016790d.png)

サビというより全体から見ておとなしいAメロの部分がスペクトログラムに反映されている


### コード
```python
import librosa
import numpy as np
import IPython.display
import librosa.display
import matplotlib.style as ms
import matplotlib.pyplot as plt
ms.use('seaborn-muted')

audio_path = 'mp3/fortune.mp3'

# 波形情報をy, サンプリングレートをsrに格納
y, sr = librosa.load(audio_path)
# スペクトログラム作成
S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)

# 先ほどのメルスペクトログラムをdBに変換
dB = librosa.logamplitude(S, ref_power=np.max)


# 以下描画
plt.figure(figsize=(12,4))

librosa.display.specshow(dB, sr=sr, x_axis='time', y_axis='mel')
plt.title('Mel Power Spectrogram')
plt.colorbar(format='%+0.20f dB')
plt.show()
```


