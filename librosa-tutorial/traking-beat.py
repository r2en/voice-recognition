# ビートをトラッキング(分離)する
from __future__ import print_function
import librosa

# librosaで準備されているサンプル曲のファイル名を取得
filename = librosa.util.example_audio_file()

# y = 波形情報 sr = サンプリングレート
y, sr = librosa.load(filename)

# デフォルトのビートトラッカーを実行
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

# ビートイベントの発生したフレーム索引をタイムスタンプへ変換
beat_times = librosa.frames_to_time(beat_frames,sr = sr)

#print('saveing output to beat_times.csv')
librosa.output.times_csv('beat_times.csv', beat_times)
