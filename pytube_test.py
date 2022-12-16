from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("failed to download video!!!!!!!")
    print("YES!!! downloaded!!!!")

link = input("enter link url here: ")
Download(link)