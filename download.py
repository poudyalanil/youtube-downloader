import youtube_dl
import subprocess

def download():
    #youyube video url
    video_url  = input("Video Url: ")

    #download
    video_info = youtube_dl.YoutubeDL().extract_info(
        video_url,download=False
    )
    file_name = f"{video_info['title']}.mp3"
    options = {
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':file_name,
        #conversion
        'postprocessors':[{
            'key':'FFmpegExtractAudio',
            'preferredcodec':'mp3',
            'preferredquality':'192',
        }]
    }
    
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])


    #play after download
    subprocess.call(["open",file_name])

if __name__ == '__main__':
    download()