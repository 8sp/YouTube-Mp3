# LIBRARIES
import youtube_dl

def run(video_url):
    try:
        video_info = youtube_dl.YoutubeDL().extract_info(
            url = video_url,download=False
        )
        filename = f"{video_info['title']}.mp3"
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':filename,
        }
    # WITH STATEMENT
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
            return  filename
    except Exception as e:
        return False