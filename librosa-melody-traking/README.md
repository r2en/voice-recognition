# LibROSAを使った楽曲構成分析器

### 前回までのあらすじ
前回はLibROSAを使ったスペクトログラムにより楽曲のどの部分がサビっぽいのかどうか特徴を探したが、あまりわからなかった。楽曲によってはAメロ(1曲を通しておとなしい部分)を見つけることができたのであった。

### 今週のLibROSA
今回は抽出したスペクトログラムのデータをクラスタリングして楽曲の構成を判断する。
前回に引き続き利用した楽曲は「はなまるピッピはよいこだけ」と「前前前世」の2曲。

### 検証

#### はなまるピッピはよいこだけ

1回目のクラスタリング
また、ほぼ平坦なグラフになるかと思ったら、今回は暴れ馬だった。特徴としてあっているのは、Aメロが10秒と60秒の部分にきているのが辛うじて判断できる。また、100秒は伴奏のみの演奏なので、そこもなんとなく判断できていそうな感じがする。それ以降のちょっと変化をつけながらのサビとかに関しては全く　違いうグラフと色を表しているため失敗かな。

![osomatu_clustring](https://user-images.githubusercontent.com/28590220/28955311-c2f5cc66-7920-11e7-86e0-2a32ae4b42fb.png)

2回目のクラスタリング
2回することにより、より楽曲構成っぽさが見えてくる。しかし、Aメロが上と比べると消失している。その代わりにサビの部分が復活している。より特徴的な部分だけを色付けしている。
![osomatu_reclustring](https://user-images.githubusercontent.com/28590220/28955313-c3196040-7920-11e7-9128-b82a31b782b2.png)

#### 前前前世

1回目のクラスタリング
きちんと音楽構成がdBで表されていたり優秀な前前前世。さすがで、クラスタリング一回でだいぶどんな音楽構成なのかが見える。紫がAメロで、サビがオレンジ色と朱色。伴奏は青色で、最後はオレンジ朱色のサビでまとめていることが一発でわかる。えらい。
![zense_clustring](https://user-images.githubusercontent.com/28590220/28955312-c3164838-7920-11e7-880f-4fbcbb04b63a.png)

2回目のクラスタリング
静かな部分が水色で示されて、サビなどが全て白色で示された。
![zense_reclustring](https://user-images.githubusercontent.com/28590220/28955314-c319e51a-7920-11e7-9baa-e6a04540222d.png)

### コード

短時間フーリエ変換をしてからスペクトログラム表示。
そのあと、クラスタリングして色付け。
もう一度クラスタリングして色付け。

```python
import math
import librosa
import datetime
import numpy as np
import pandas as pd
import seaborn as sns
import librosa.display
import IPython.display
import matplotlib.pyplot as plt
import matplotlib.colors as clrs
from sklearn import cluster

audio_path = 'mp3/osomatu.mp3'
music, fs = librosa.audio.load(audio_path)

def reclustering(data_frame):
    k_means_music = cluster.KMeans(n_clusters=4)
    k_means_music.fit(data_frame)
    data_frame['cluster'] = k_means_music.labels_

    re_data = from_labels_to_dataframe(k_means_music.labels_)
    re_data_list = shape_data_frame(re_data)
    colors = matplot_colors(re_data)
    show_stackplot(data_frame, re_data_list, colors)

def from_labels_to_dataframe(labels_list):
    labels_pd_list = []
    for i in range(len(labels_list)):
        labels_pd_list.append(np.bincount([labels_list[i]]))
    return pd.DataFrame(labels_pd_list)

def show_stackplot(data_frame, pd_data_list, colors):
    figure, axes = plt.subplots(1, 1, figsize=(15,5))
    figure.patch.set_facecolor('white')
    axes.stackplot(data_frame.index, pd_data_list, colors=colors)
    plt.xticks([i*10 for i in range(int(round(data_frame.index.tolist()[-1]))//10 + 1)])
    plt.show()

def shape_data_frame(data_frame):
    pd_data_frame_list = []
    for i in range(len(data_frame.columns)):
        pd_data_frame_list.append(data_frame[i])
    return pd_data_frame_list

def matplot_colors(data_frame):
    return list(clrs.cnames.values())[:len(data_frame.columns)]

def main():
    # 短時間フーリエ変換
    d = librosa.stft(music, n_fft=2048, hop_length=(2048//4), win_length=None)
    dB = librosa.logamplitude(np.abs(d)**2,ref_power=np.max)
    librosa.display.specshow(dB,y_axis='log',x_axis='time',hop_length=(2048//4))

    plt.title('Power spectrogram')
    plt.colorbar(format='%+2.0f dB')
    # plt.show()

    # クラスタリング
    cluster_rabel = 50
    k_means = cluster.KMeans(n_clusters=20)
    k_means.fit(dB.T)
    k_means_culumns = k_means.labels_.shape[0]

    count_data_list = []

    for i in range(k_means_culumns//cluster_rabel):
        data = k_means.labels_[i*cluster_rabel:(i+1)*cluster_rabel]
        count_data = np.bincount(data)
        count_data_list.append(count_data)

    index = [(len(music)/fs)/len(count_data_list) * data for data in range(len(count_data_list))]
    data_frame = pd.DataFrame(count_data_list, index = index).fillna(0)

    columns = [chr(i) for i in range(65, 65+26)][:10]

    pd_data_list = shape_data_frame(data_frame)
    colors = matplot_colors(data_frame)
    show_stackplot(data_frame, pd_data_list, colors)
    reclustering(data_frame) 

if __name__ == '__main__':
    main()


```

### まとめ
どの楽曲に対してもなんとなく、わかるわかるって気持ちになる画像をクラスタリングするとくれるが、精度としてはイマイチ。
