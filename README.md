# 概要

Pythonのライブラリ「pytube」を使った、YouTubeの動画をダウンロードするアプリです。  
お使いのPCにPythonがインストールされていなくても動作可能ですが、  
ffmpegをインストールし、環境変数に設定する必要があります。  
従来の[youtube-dl](https://ja.wikipedia.org/wiki/Youtube-dl)と比べて、pytubeの方が高速にダウンロードできます。  
クリエイティブ・コモンズ認可済みの動画はダウンロードしても何の問題もありません。  
それ以外の動画をダウンロードすることはYouTubeの利用規約に反するので自己責任でお願いします。  
また、YouTubeに違法アップロードされている動画のダウンロードは違法です。

# ダウンロード

アプリのダウンロードは[こちら]()。

ffmpegのインストール方法は[こちら](https://github.com/yuusanx3/knowledge/wiki/ffmpeg_install)。

# 使用方法

## 準備と起動

1. zipでダウンロードした場合は解凍します。

2. `build/`にある、`PYTUBE Downloader`のフォルダを任意の場所に置いてください。 
 
3. その中にある、`main.exe`をダブルクリックします。

   > Python環境のある方はルートディレクトリで、`python main.py`でも実行できます。

## 基本的な使用方法

![image](https://user-images.githubusercontent.com/123562334/215416215-db24ccc9-03ee-4fc8-93cf-71438e74dcc7.png)

1. 後ろに表示されたYouTubeブラウザでダウンロードしたい動画を検索します。

2. ダウンロードしたい動画のページに入り、右下の`URLを反映`ボタンを押します。  
すると、URLがメインウィンドウの`動画URL`の欄に反映されます。

3. PC内の保存先フォルダを指定します。  
フォルダパスをエクスプローラからコピペしてください。

4. メインウィンドウ左下の`ダウンロード`の枠内にあるボタンのいずれかをクリックします。  
   1. 映像と音声を一緒にダウンロードしたい場合（普通はコレ）  
      `動画＋音声`のボタンをクリックします。
   2. 映像のみをダウンロードしたい場合（声無しです）  
      `動画のみ`のボタンをクリックします。
   3. 音声のみをダウンロードしたい場合（音楽などの場合）  
      `音声のみ`のボタンをクリックします。<br><br>
   
   > 動画＋音声の場合、ダウンロード可能な最高の画質と音質でダウンロードされます。  
   > 動画のみの場合、ダウンロード可能な最高の画質でダウンロードされます。  
   > 音声のみの場合、タグ管理のしやすい.m4aのうちダウンロード可能な最高の音質でダウンロードされます。  
   > ダウンロード中はUIが固まりますが、裏でちゃんと動いています（笑）  
   > 10分くらいの動画になると結構待ちます。最初は2分程度の短い動画で試してみてください。
   
## 画質や音質を指定してダウンロードする

1. URL入力後、`形式を選択してダウンロード`の枠内にある、`ファイル情報取得`ボタンをクリックします。

2. プルダウンメニューから、画質を選択します。

3. `ダウンロード`ボタンをクリックします。

   > この方法では、動画と音声は同時にダウンロードできないので、ご自身でmuxしてください。  
   > ffmpegのCUIでmuxしてもいいですが、[MKVToolNix GUI](https://www.gigafree.net/media/me/mkvtoolnix.html)もおすすめです。

# Pythonライブラリ「pytube」の使い方

## pytubeのインストール

```cmd
pip install pytube
```

## ざっくりした使い方

まず、プログラムの先頭に以下を記述
```py
from pytube import YouTube
```

### 何でもいいからダウンロードする

```py
YouTube({ダウンロードしたい動画のURL}).streams.first().download({動画を保存するフォルダのパス})
```

### 形式を選択してダウンロードする

1. ダウンロード可能な形式のリストを表示
   ```py
   download_list = YouTube({ダウンロードしたい動画のURL}).streams
   print(download_list)
   ```

2. ダウンロードする
   ```py
   YouTube({ダウンロードしたい動画のURL}).streams.get_by_itag({1.のリストの中のitag番号}).download({動画を保存するフォルダのパス})
   ```

# 最後に

要望、不具合等あれば、TwitterのDMにお願いします。  
気が向いたら修正するかもしれません。
