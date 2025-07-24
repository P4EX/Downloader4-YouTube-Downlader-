```
M""""""'YMM                              dP                         dP                   dP   dP 
M  mmmm. `M                              88                         88                   88   88 
M  MMMMM  M .d8888b. dP  dP  dP 88d888b. 88 .d8888b. .d8888b. .d888b88 .d8888b. 88d888b. 88aaa88 
M  MMMMM  M 88'  `88 88  88  88 88'  `88 88 88'  `88 88'  `88 88'  `88 88ooood8 88'  `88      88 
M  MMMM' .M 88.  .88 88.88b.88' 88    88 88 88.  .88 88.  .88 88.  .88 88.  ... 88            88 
M       .MM `88888P' 8888P Y8P  dP    dP dP `88888P' `88888P8 `88888P8 `88888P' dP            dP 
MMMMMMMMMMM                                                                                      

A simple YouTube MP3/MP4 and Playlists Downloader                                                                                          
                                                                                                                               
```
                                                                                              
---

## Features
- Download single YouTube videos as MP3 or MP4
- Download all audios from a YouTube playlist as MP3
- Simple interactive menu
- Output files saved in `downloader/media/mp3/` and `downloader/media/mp4/`

## Requirements
- Python 3.7+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [ffmpeg](https://ffmpeg.org/) (must be installed on your system)

## Installation
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Make sure ffmpeg is installed and available in your PATH.

## Usage
Run the script from the `downloader` directory:
```bash
python downloader.py
```
Follow the menu to select download options.

## Project Structure
- `downloader.py` - Main script
- `media/mp3/` - Downloaded MP3 files
- `media/mp4/` - Downloaded MP4 files
- `requirements.txt` - Python dependencies

## License
MIT

## Credits
- Built with [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- Banner art by @Kairan (P4EX)
