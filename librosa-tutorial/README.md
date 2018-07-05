# LibROSAチュートリアル


![image](https://user-images.githubusercontent.com/28590220/28956116-ee377410-7925-11e7-89b4-02e4f9e5b13f.png)



### 特徴
- SPTK
    基礎: フーリエ変換やリサンプリング等、音声信号処理や音声認識など豊富なコマンドが用意されている。
- LibROSA
    応用: MIR(音楽情報検索)を意識し、音楽分析や加工分離を得意としている。より実用的な位置にいる。ビジネスになりそうなものが多く用意されている。2015年にリリースされた。


### 開発環境

PC環境
- macOS Sierra ver 10.12

Python環境
- anyenv
    - pyenv
        - anaconda3-4.3.1


### インストール
```python
$ pip install librosa
```

### 動作確認
LibROSAの　[チュートリアルクイックスタート](http://librosa.github.io/librosa/tutorial.html)をやってみる

これは楽曲からビートを検出してCSV出力するサンプル

```python

# ビートをトラッキング(分離)する
from __future__ import print_function
import librosa

# librosaで準備されているサンプル曲のファイル名を取得
filename = librosa.util.example_audio_file()

# y = 波形情報 sr = サンプリングレート
y, sr = librosa.load(filename)

# デフォルトのビートトラッカーを実行
tempo, beat_frames = librosa.beat.beat_track(y=y,sr=sr)

print('Estimated temp:{:.2f}beats per minute'.format(tempo))

# ビートイベントの発生したフレーム索引をタイムスタンプへ変換
beat_times = librosa.frames_to_time(beat_frames,sr = sr)


print('saveing output to beat_times.csv')
librosa.output.times_csv('beat_times.csv', beat_times)

```

実行結果


> Estimated tempo: 129.20 beats per minute
Saving output to beat_times.csv


1分間に129ビートが判明した。csvファイルにはビート検出時の楽曲開始からの秒数を出力させている。

>0.116
0.557
0.998
1.463
1.927
2.392
2.833
3.297
3.762
4.226
4.690
5.155
5.619
6.084
6.525




























