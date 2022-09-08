# Program allows to download video from YouTube for off-line watching
# pytube library is used
# Current limitation is 720p :(

import os.path
from pathlib import Path
from art import tprint
from pytube import YouTube
import ffmpeg

def youtube_downloader():    
    # Ask user to provide link to the target video
    youtube_link = input('\nEnter link to the targer video: ')

    # Double check if we have "Output" folder. If not, then create one
    path = Path(__file__).absolute()
    
    if not os.path.isdir('./Output'):
        os.mkdir('./Output')
        print(f'[+] Output folder has been created')

    # Create an object of YouTube class
    yd = YouTube(youtube_link).streams.get_highest_resolution()

    # Download video
    print(f'[+] Video is downloading')
    yd.download('./Output')
    print(f'[+] Video has been downloaded')

def main():
    tprint('YouTube Downloader', font='bulbhead')
    youtube_downloader()

if __name__ == '__main__':
    main()
