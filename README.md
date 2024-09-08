# YouTube Video Downloader using yt-dlp

## Description

This Python script allows you to list available formats for a YouTube video and download the video in the selected formats using the `yt-dlp` library. The script lists various details about the available formats, such as video resolution, bitrate, frame rate (FPS), and codecs, and then downloads the video in two user-specified formats.

## Features

- **List Available Formats**: The script retrieves and displays the available video formats, including format code, resolution, audio bitrate, frame rate (FPS), and codecs.
- **Download in Multiple Formats**: Users can download a video in two different formats by specifying the format codes.
- **Flexible Output**: The downloaded files are saved with a naming convention that includes the video title and format code.

## Requirements

- **Python 3.6+**
- **yt-dlp**: A command-line tool and Python library for downloading videos from YouTube and other video platforms.

### Installation of Dependencies

To install the `yt-dlp` library, run the following command:

```bash
pip install yt-dlp
```

## Usage

1. **Clone the repository** or copy the script file to your local machine.
   
2. **Run the script**:
   
   ```bash
   python downloader.py
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

### Example

```bash
Enter the URL of a YouTube video: https://www.youtube.com/watch?v=example
Available formats:
Format code: 22, Extension: mp4, Resolution: 720p, Bitrate: N/A kbps, FPS: 30, Video codec: avc1.64001F, Audio codec: mp4a.40.2, Note: 
...
Enter two desired format codes to download the video (e.g., '22,18'): 22,18
Download completed successfully for format code: 22.
Download completed successfully for format code: 18.
```

## Script Breakdown

- **`list_formats(url)`**: Extracts and lists the available formats for a given YouTube video URL, displaying details such as format code, extension, resolution, bitrate, FPS, and codecs.
  
- **`download_video(url, format_codes)`**: Downloads the video in the specified formats. The files are saved in the current directory, with filenames that include the video title and format code.

## Notes

- Ensure that you have an active internet connection while using this script, as it relies on the YouTube platform to fetch video details and download videos.
- The script is designed to download videos in two different formats, but it can be easily modified to handle more formats.

## License

This project is licensed under the MIT License.
