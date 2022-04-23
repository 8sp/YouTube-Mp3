# Copyright © 2022 All Rights Reserved
# Developed & Programmed By Null
# For More Information Contact @entrysquad (IG)

import youtube_dl
import os
import colorama
from colorama import Fore
from os import system
colorama.init(autoreset=True)
system("title " + "YouTube Mp3 Downloader - By Null")

# Null
logo = f"""     
   _   _       _ _ 
  | \ | |_   _| | |
  |  \| | | | | | |
  | |\  | |_| | | |
  |_| \_|\__,_|_|_| {Fore.WHITE}(v1.0){Fore.RESET}
"""
print(Fore.CYAN+logo)

# Def Function
def run():
    video_url = input(f"[{Fore.MAGENTA}?{Fore.RESET}] YouTube Video Url: ")
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }
# With Statement   
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print(f"[{Fore.GREEN}+{Fore.RESET}] Successfully Downloaded & Saved In>> ",("{}".format(filename))) 
    print

if __name__=='__main__':
    run()
# End Codding
