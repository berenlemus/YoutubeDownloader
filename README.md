# Youtube Video Downloader

## Description
This Python application allows users to download YouTube videos by entering the video link. It utilizes the pytube library to fetch the video from YouTube and download it to the local system.

## Usage
1. Run the Python script (`youtube_downloader.py`).
2. Enter the YouTube video link in the provided text entry field.
3. Click the "DOWNLOAD VIDEO" button to start the download process.
4. Upon successful download, a message will be displayed confirming the download.

## Requirements
- tkinter library (usually comes pre-installed with Python)
- pytube library (install using `pip install pytube`)

## Files
- `youtube_downloader.py`: The main Python script.
- `README.md`: This file providing information about the application.

## Note
- Ensure that you have a working Python environment with the tkinter and pytube libraries installed.
- The application downloads the highest resolution version of the YouTube video.
- You can specify the download location by modifying the `video.download()` line in the `download_video()` function.

## Credits
- Inspired by various tutorials and resources on building YouTube video downloader applications with Python and tkinter.

