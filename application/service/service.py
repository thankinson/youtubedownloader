from pytube import YouTube

class DownloadChoice():
    def VideoDownload(link):
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        try:
            youtubeObject.download()
        except:
            return 'Download Failed!!!'
        return 'YES!!! Video Downloaded!!!!'

    def AudioDownload(link):
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_audio_only()
        try:
            youtubeObject.download()
        except:
            return 'Download Failed!!!'
        return 'YES!!! Audio Downloaded!!!!'