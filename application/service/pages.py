from flask import redirect, url_for, render_template, request
from application.forms.forms import DownLoadVideo, DownLoadAudio
from application.service.service import DownloadChoice

class IndexPage():
    def Index():
        return render_template('index.html')

class DownloadPage():
    def Download():
        video = DownLoadVideo()
        audio = DownLoadAudio()
        if video.validate_on_submit():
            return DownloadChoice.VideoDownload(link=video)
        if audio.validate_on_submit():
            return DownloadChoice.AudioDownload(link=audio)
        return render_template('download.html', formvid=video, formaudio=audio)