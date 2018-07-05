## Voice_Recognition 音声認識

OS ： OSX Yosemite ver.10.10.5<br>

Python ： Python 2.7.13<br>

Python Module Library：pyaudio,numpy, pylab, SPTK, gnuplot, scipy, sklearn, librosa<br>

※ python2系と3系ではfp.read()などの戻り値の型が異なる為、2系を推奨<br>

現在の環境

OS ： OSX Sierra ver.10.12.6<br>

Python: Python 3.6.0 :: Anaconda 4.3.1 (x86_64)


## Install: 導入

音声加工分離ライブラリ<br>

[LibROSA インストールガイド](https://github.com/whitetokyo/r-d/tree/master/voice-recognition/librosa-tutorial)

## Reseach: 基礎研究<br>

[・Voise Signal Processing[音声信号処理]](https://github.com/whitetokyo/r-d/tree/master/voice-recognition/voice-signal-processing)<br>

音声波形、フーリエ変換やケプストラム分析、線形予測分析等の音声認識基幹技術を調査しているページ

<br>


[・SPTK](https://github.com/whitetokyo/r-d/tree/master/voice-recognition/signal-processing-toolkit)<br>
基礎: フーリエ変換やリサンプリング等、音声信号処理や音声認識など豊富なコマンドが用意されている。

<br>

[・LibROSA](https://github.com/whitetokyo/r-d/tree/master/voice-recognition/librosa)<br>

応用: MIR(音楽情報検索)を意識し、音楽分析や加工分離を得意としている。より実用的な位置にいる。ビジネスになりそうなものが多く用意されている。2015年にリリースされた。

<br>

## Survey: 商品開発調査<br>

音声認識のAPI,音声認識のソフトの比較,競業他社などを調査<br>

[市場調査](https://github.com/whitetokyo/r-d/tree/master/voice-recognition/survey)

<br>


## Paper: 論文リスト<br>


[音声認識関連の論文](https://github.com/whitetokyo/r-d/tree/master/voice-recognition/survey)

<br>


## Development: 実装<br>

周波数分析
- [ライブ盛り上がり判定](https://github.com/whitetokyo/r-d/tree/master/voice-recognition/librosa-spectrogram)
- [音源分離](https://github.com/whitetokyo/r-d/tree/master/voice-recognition/librosa-music-separation)
- [楽曲構成分析](https://github.com/whitetokyo/r-d/tree/master/voice-recognition/librosa-melody-traking)

音楽情報検索
- [音楽情報検索](https://github.com/whitetokyo/r-d/tree/master/voice-recognition/static-voicec-conversion)

統計的性質変換


