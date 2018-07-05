# SOX(Sound eXchange)を使ったスペクトログラム

今回はLibROSAを使ったスペクトログラムをあげたが、精度と手間どちらも圧勝したのが[SOX](http://sox.sourceforge.net/)。

オーディオ変換は基本的になんでもこなしてくれる。

### インストール方法

```python
brew install lame
brew install sox
```

### 使い方
例えばmp3をピッチそのままで1.5倍速に変換したければ
```python
sox src.mp3 dst.mp3 tempo 1.5
```
これ一行...。

<br>

今回の苦労して書いたスペクトログラムは
```python
sox osomatu.mp3 -n spectrogram
```
のみ。

<br>

### 検証

1.はなまるぴっぴはよいこだけ
先ほどより、変化が見られる。弱い部分は伴奏。

![sox_osomatu](https://user-images.githubusercontent.com/28590220/28951767-0d0ea7f0-7908-11e7-82e6-ba49207afea9.png)

<br>

2.前前前世
この曲は完璧すぎるが、Aメロが本当に綺麗に別れている。

![sox_zense](https://user-images.githubusercontent.com/28590220/28951768-0d1b9dd4-7908-11e7-9e95-d431d578c5b3.png)


### 結論
LibROSAよりもSOX