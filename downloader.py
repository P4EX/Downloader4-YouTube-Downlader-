import yt_dlp

RED = "\033[31m"
WHITE = "\033[37m"
GREEN = "\033[32m"
RESET = "\033[0m"

def banner():
    """
    Prints the welcome banner and main menu options with ANSI colors.
    """
    print(f"""{RED}
    ____                      __                __         
   / __ \____ _      ______  / /___  ____ _____/ /__  _____
  / / / / __ \ | /| / / __ \/ / __ \/ __ `/ __  / _ \/ ___/
 / /_/ / /_/ / |/ |/ / / / / / /_/ / /_/ / /_/ /  __/ /    
/_____\/____/|__/|__/_/ /_/_/\____/\__,_/\__,_/\___/_/ 1.0 {WHITE} Made By @Kairan (P4EX)

          

{WHITE}[+] 1. {RESET} Download MP3 From YouTube    
{WHITE}[+] 2. {RESET} Download MP4 From YouTube
{WHITE}[+] 3. {RESET} Download MP3 From YouTube (Playlist) 

{WHITE}[+] 4. Exit

{RESET}                                                                              
""", end="\r")


def downloadMp4():
    """
    Download a YouTube video as MP4 (video+audio) to media/mp4.
    Asks for URL, shows status, handles errors, allows retry or menu.
    """
    while True:
        try:
            url = input(f"{WHITE}[+]{RESET} Enter URL: ")
            ydl_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
                'outtmpl': 'downloader/media/mp4/%(title)s.%(ext)s',
                'noplaylist': True
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                print(f"{GREEN}[+]{RESET} {info.get('title', 'Video')} downloaded.")
            break
        except Exception as e:
            print(f"{RED}[+]{RESET} Error in Download MP4: {e}")
        if input(f"{WHITE}[+]{RESET} Try again? (Y/n)").lower() != "y":
            break
    main()

def downloadMp3():
    """
    Download YouTube audio as MP3 to downloader/media/mp3.
    Asks for URL, shows status, handles errors, allows retry or menu.
    """
    while True:
        try:
            url = input(f"{WHITE}[+]{RESET} Enter URL: ")
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': 'downloader/media/mp3/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'noplaylist': True
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                print(f"{GREEN}[+]{RESET} {info.get('title', 'Audio')} downloaded.")
            break
        except Exception as e:
            print(f"{RED}[+]{RESET} Error in Download MP3: {e}")
        if input(f"{WHITE}[+]{RESET} Try again? (Y/n)").lower() != "y":
            break
    main()

def downloadMp3Pl():
    """
    Download all audios from a YouTube playlist as MP3 to downloader/media/mp3/playlist_name.
    Asks for playlist URL, shows status, handles errors, allows retry or menu.
    """
    while True:
        try:
            url = input(f"{WHITE}[+]{RESET} Enter Playlist URL: ")
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': 'downloader/media/mp3/%(playlist_title)s/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'noplaylist': False
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                print(f"{GREEN}[+]{RESET} Playlist '{info.get('title', 'Playlist')}' downloaded.")
            break
        except Exception as e:
            print(f"{RED}[+]{RESET} Error in Download Playlist: {e}")
        if input(f"{WHITE}[+]{RESET} Try again? (Y/n)").lower() != "y":
            break
    main()

def main():
    """
    Show main menu, get user option, call the selected function.
    If invalid option, show menu again.
    """
    banner()
    des = input(f"{GREEN}>>> ")
    if des == "1":
        downloadMp3()
    elif des == "2":
        downloadMp4()
    elif des == "3":
        downloadMp3Pl()
    elif des == "4":
        exit()
    else:
        print(f"{RED}[+]{RESET} Try Again.")
        main()

main()