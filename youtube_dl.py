#---------------------------------------------------------------------------------------------------
# YouTubeから動画をダウンロードする
# pytubeを利用
# pip install pytube
# pip install ffmpeg-python
#---------------------------------------------------------------------------------------------------
from pytube import YouTube
import ffmpeg
import os
import traceback
from datetime import datetime
import logging

LOG_FILE_PATH = "./logs/youtube_dl.log"

class Log:
    def __init__(self,log_path):
        if False == os.path.exists(os.path.dirname(log_path)):
            os.mkdir(os.path.dirname(log_path))
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s [%(levelname)s]: %(message)s')
        file_handler = logging.FileHandler(log_path, encoding="UTF-8")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger

class Main:
    def __init__(self) -> None:
        self.log = Log(LOG_FILE_PATH)
        self.logger = self.log.get_logger()

class Youtube(Main):
    def __init__(self,url) -> None:
        super().__init__()
        self.url = url

    # 動画+音声をダウンロードする
    def download(self,folder_path):
        try:
            # ダウンロードリスト
            download_list = YouTube(self.url).streams
            # 動画
            video_mode = None
            # 音声
            audio_mode = None
            for p in download_list:
                # 最も画質の良い動画を選択
                if "video" == p.type:
                    if None == video_mode or int(video_mode.resolution.rstrip("p")) < int(p.resolution.rstrip("p")) or (
                        int(video_mode.resolution.rstrip("p")) == int(p.resolution.rstrip("p")) and
                        int(video_mode.bitrate) < int(p.bitrate)):
                        # 解像度が高い動画を優先 解像度が同じであればビットレートの高い動画を優先
                        video_mode = p
                # 最も音質の良い音声を選択
                if "audio" == p.type:
                    if None == audio_mode or int(audio_mode.bitrate) < int(p.bitrate):
                        audio_mode = p
            # 動画をダウンロードする
            file_path_dl = YouTube(self.url).streams.get_by_itag(video_mode.itag).download(folder_path)
            file_path_video = folder_path + "\\" + datetime.now().strftime("%Y%m%d%H%M%S%f")
            # ダウンロードしたものをリネーム
            os.rename(
                file_path_dl,
                file_path_video
            )
            # 音声をダウンロードする
            file_path_dl = YouTube(self.url).streams.get_by_itag(audio_mode.itag).download(folder_path)
            file_path_audio = folder_path + "\\" + datetime.now().strftime("%Y%m%d%H%M%S%f")
            # ダウンロードしたものをリネーム
            os.rename(
                file_path_dl,
                file_path_audio
            )
            muxed_file = file_path_dl.rstrip(file_path_dl.split(".")[-1]) + "mkv" # 完成ファイル名
            # ffmpegでmux
            ffmpeg_video = ffmpeg.input(file_path_video).video
            ffmpeg_audio = ffmpeg.input(file_path_audio).audio
            stream = ffmpeg.output(ffmpeg_video, ffmpeg_audio, muxed_file, vcodec="copy", acodec="copy")
            ffmpeg.run(stream, overwrite_output=True)
            # 残った一時ファイルを削除
            os.remove(file_path_video)
            os.remove(file_path_audio)
            return {"code":0, "message":"", "file_path":muxed_file}
        except:
            self.logger.error(traceback.format_exc())
            return {"code":1, "message":"処理に失敗しました"}

    # 動画をダウンロードする
    def download_video(self,folder_path):
        try:
            # ダウンロードリスト
            download_list = YouTube(self.url).streams.filter(only_video=True)
            video_mode = None
            extension = None # 拡張子
            for p in download_list:
                # 最も画質の良い動画を選択
                if "video" == p.type:
                    if None == video_mode or int(video_mode.resolution.rstrip("p")) < int(p.resolution.rstrip("p")) or (
                        int(video_mode.resolution.rstrip("p")) == int(p.resolution.rstrip("p")) and
                        int(video_mode.bitrate) < int(p.bitrate)):
                        # 解像度が高い動画を優先 解像度が同じであればビットレートの高い動画を優先
                        video_mode = p
            # m4aがあればそちらを優先
            if "avc1" in video_mode.video_codec:
                extension = "mp4"
            elif "vp9" in video_mode.video_codec:
                extension = "webm"
            # ダウンロードする
            file_path_dl = YouTube(self.url).streams.get_by_itag(video_mode.itag).download(folder_path)
            file_path_video = folder_path + "\\" + datetime.now().strftime("%Y%m%d%H%M%S%f")
            # ダウンロードしたものをリネーム
            os.rename(
                file_path_dl,
                file_path_video
            )
            muxed_file = file_path_dl.rstrip(file_path_dl.split(".")[-1]) + extension # 完成ファイル名
            # ffmpegでmux
            ffmpeg_video = ffmpeg.input(file_path_video).video
            stream = ffmpeg.output(ffmpeg_video, muxed_file, vcodec="copy")
            ffmpeg.run(stream, overwrite_output=True)
            # 残った一時ファイルを削除
            os.remove(file_path_video)
            return {"code":0, "message":"", "file_path":muxed_file}
        except:
            self.logger.error(traceback.format_exc())
            return {"code":1, "message":"処理に失敗しました"}

    # 音声をダウンロードする
    def download_audio(self,folder_path):
        try:
            # ダウンロードリスト
            download_list = YouTube(self.url).streams.filter(only_audio=True)
            audio_mode = None
            m4a_mode = None
            opus_mode = None
            extension = None # 拡張子
            for p in download_list:
                # 最も音質の良い音声を選択
                if "mp4a" in p.audio_codec:
                    if None == m4a_mode or int(m4a_mode.bitrate) < int(p.bitrate):
                        m4a_mode = p
                if "opus" in p.audio_codec:
                    if None == opus_mode or int(opus_mode.bitrate) < int(p.bitrate):
                        opus_mode = p
            # m4aがあればそちらを優先
            if None == m4a_mode:
                audio_mode = opus_mode
                extension = "opus"
            else:
                audio_mode = m4a_mode
                extension = "m4a"
            # ダウンロードする
            file_path_dl = YouTube(self.url).streams.get_by_itag(audio_mode.itag).download(folder_path)
            file_path_audio = folder_path + "\\" + datetime.now().strftime("%Y%m%d%H%M%S%f")
            # ダウンロードしたものをリネーム
            os.rename(
                file_path_dl,
                file_path_audio
            )
            muxed_file = file_path_dl.rstrip(file_path_dl.split(".")[-1]) + extension # 完成ファイル名
            # ffmpegでmux
            ffmpeg_audio = ffmpeg.input(file_path_audio).audio
            stream = ffmpeg.output(ffmpeg_audio, muxed_file, acodec="copy")
            ffmpeg.run(stream, overwrite_output=True)
            # 残った一時ファイルを削除
            os.remove(file_path_audio)
            return {"code":0, "message":"", "file_path":muxed_file}
        except:
            self.logger.error(traceback.format_exc())
            return {"code":1, "message":"処理に失敗しました"}

    # ダウンロードリストを表示する
    def show_list(self):
        try:
            download_dict_list = []
            download_Stream_list = YouTube(self.url).streams.filter()
            for p in download_Stream_list:
                download_dict = {}
                download_dict["itag"] = p.itag
                data = "type=\"" + p.type
                if "video" ==  p.type:
                    data += "\" codec=\"" + p.video_codec
                    data += "\" bitrate=\"" + "{:.1f}".format(float(p.bitrate)/1024.0) + "kbps"
                    data += "\" resolution=\"" + p.resolution
                    data += "\" fps=\"" + str(p.fps) + "\""
                elif "audio" == p.type:
                    data += "\" codec=\"" + p.audio_codec
                    data += "\" bitrate=\"" + "{:.1f}".format(float(p.bitrate)/1024.0) + "kbps\""
                download_dict["data"] = data
                download_dict_list.append(download_dict)
            return {"code":0, "message":"" , "data":download_dict_list}
        except:
            self.logger.error(traceback.format_exc())
            return {"code":1, "message":"処理に失敗しました"}

    # 画質、音質を選択してダウンロードする
    def download_by_itag(self,itag,folder_path):
        try:
            extension = None
            download_mode = YouTube(self.url).streams.get_by_itag(itag)
            if "video" == download_mode.type:
                if "avc1" in download_mode.video_codec:
                    extension = "mp4"
                elif "vp9" in download_mode.video_codec:
                    extension = "webm"
            # ダウンロードしたものをリネーム
            elif "audio" == download_mode.type:
                if "mp4a" in download_mode.audio_codec:
                    extension = "m4a"
                if "opus" in download_mode.audio_codec:
                    extension = "opus"
            file_path_dl = download_mode.download(folder_path)
            file_path_ffmpeg_in = folder_path + "\\" + datetime.now().strftime("%Y%m%d%H%M%S%f")
            # ダウンロードしたものをリネーム
            os.rename(
                file_path_dl,
                file_path_ffmpeg_in
            )
            muxed_file = file_path_dl.rstrip(file_path_dl.split(".")[-1]) + extension # 完成ファイル名
            # ffmpegでmux
            ffmpeg_in = ffmpeg.input(file_path_ffmpeg_in)
            stream = ffmpeg.output(ffmpeg_in, muxed_file, vcodec="copy", acodec="copy")
            ffmpeg.run(stream, overwrite_output=True)
            # 残った一時ファイルを削除
            os.remove(file_path_ffmpeg_in)
            return {"code":0, "message":"", "file_path":muxed_file}
        except:
            self.logger.error(traceback.format_exc())
            return {"code":1, "message":"処理に失敗しました"}
