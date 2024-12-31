# YouTube Video Downloader and Audio Extractor using yt-dlp

## Description

This repository includes Python scripts for downloading and processing content from YouTube using the `yt-dlp` library. In addition to the original video downloader script, a new script, `YT_Audio_Downloader.py`, is now available for downloading audio tracks and converting them to high-quality MP3 format.

### Video Downloader
The `YT_Video_Downloader.py` script allows you to list available formats for a YouTube video and download the video in the selected formats. The script lists various details about the available formats, such as video resolution, bitrate, frame rate (FPS), and codecs, and then downloads the video in two user-specified formats.

### Audio Downloader
The `YT_Audio_Downloader.py` script is specifically designed for downloading audio tracks from YouTube and converting them to MP3 format. It ensures high-quality downloads by selecting the best available audio format and uses `ffmpeg` to convert the downloaded audio into MP3 with a 192 kbps bitrate.

## Features

### Video Downloader
- **List Available Formats**: The script retrieves and displays the available video formats, including format code, resolution, audio bitrate, frame rate (FPS), and codecs.
- **Download in Multiple Formats**: Users can download a video in two different formats (one for video, one for audio) by specifying the format codes.
- **Flexible Output**: The downloaded files are saved with a naming convention that includes the video title and format code.

### Audio Downloader
- **High-Quality Audio**: Automatically selects the best available audio format.
- **MP3 Conversion**: Converts downloaded audio to MP3 format using `ffmpeg` with a 192 kbps bitrate.
- **Simplified Workflow**: Users only need to provide a YouTube URL, and the script handles the rest.

## Requirements

- **Python 3.6+**
- **yt-dlp**: A command-line tool and Python library for downloading videos from YouTube and other video platforms.
- **ffmpeg**: A tool for handling multimedia data, used for converting audio to MP3 in the audio downloader script.

### Installation of Dependencies

To install the `yt-dlp` library and `ffmpeg`, run the following commands:

```bash
pip install yt-dlp
# Install ffmpeg based on your system:
# For Windows: Download from https://ffmpeg.org/download.html
# For macOS: brew install ffmpeg
# For Linux: sudo apt install ffmpeg
```

## Usage

### Video Downloader

1. **Clone the repository** or copy the `YT_Video_Downloader.py` file to your local machine.
   
2. **Run the script**:
   
   ```bash
   python YT_Video_Downloader.py
   ```

3. **Input the YouTube video URL** when prompted:

   ```bash
   Enter the URL of a YouTube video: https://www.youtube.com/watch?v=example
   ```

4. The script will display a list of available formats. You need to specify two format codes to download:

   ```bash
   Enter two desired format codes to download the video (e.g., '22,18'): 22,18
   ```

5. The script will download the video in both formats and save the files to the current directory.

### Audio Downloader

1. **Clone the repository** or copy the `YT_Audio_Downloader.py` file to your local machine.

2. **Run the script**:

   ```bash
   python YT_Audio_Downloader.py
   ```

3. **Input the YouTube video URL** when prompted:

   ```bash
   Enter the URL of a YouTube video: https://www.youtube.com/watch?v=example
   ```

4. The script will download the audio in the best available format and convert it to MP3. The final MP3 file will be saved in the current directory.

### Example (Audio Downloader)

```bash
Enter the URL of a YouTube video: https://www.youtube.com/watch?v=example
Downloading and converting to MP3...
Download and conversion completed successfully.
```

## Notes

- Ensure that you have an active internet connection while using these scripts, as they rely on the YouTube platform to fetch video and audio details.
- The `YT_Audio_Downloader.py` script is optimized for audio tracks, while `YT_Video_Downloader.py` focuses on video.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](./LICENSE) file for more details.
