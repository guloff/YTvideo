This Python script leverages `yt-dlp`, a powerful command-line tool, to facilitate the downloading of YouTube videos in various formats. With an intuitive interface, the script prompts users to provide a YouTube video URL and then displays a comprehensive list of all available download formats. These formats encompass essential details such as format code, file extension, resolution, bitrate, frames per second, and both video and audio codecs, alongside any pertinent notes regarding the format. In an enhancement to its functionality, users now have the flexibility to select not just one but two format codes simultaneously, enabling the download of two different versions of a video at once. This feature significantly benefits users who require videos in multiple formats for diverse applications, including offline viewing, content archiving, or multimedia projects. The downloaded videos are conveniently saved in the script's directory, with filenames that incorporate the video title and the selected format codes, thereby simplifying file management and retrieval.

### Features:
- **User-Friendly Interface**: Simple execution flow, guiding users from URL input to downloading with ease.
- **Enhanced Download Capabilities**: Offers the ability to download videos in two different formats simultaneously, catering to varied user needs.
- **Detailed Format Information**: Provides exhaustive details on available video formats, including technical specifications like bitrate and codecs.
- **Automated File Naming**: Automatically names downloads incorporating video titles and format codes, facilitating easy identification and organization.

### How to Use:
1. Ensure Python is installed on your computer.
2. Use pip to install `yt-dlp`: run `pip install yt-dlp` in your terminal.
3. Execute the script by running `python download_youtube_video.py` from your command line.
4. When prompted, paste the URL of the YouTube video you wish to download and enter the format codes for your desired formats when requested.

This tool has been developed for educational and personal use. It is imperative that users respect YouTube's terms of service and adhere to copyright regulations when downloading content.
