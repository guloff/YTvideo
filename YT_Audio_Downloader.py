import os
import subprocess
import sys
import yt_dlp

def check_dependencies():
    try:
        import yt_dlp
    except ImportError:
        print("yt-dlp is not installed. Installing it now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
        print("yt-dlp has been installed.")

def download_and_convert_to_mp3(url):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_template = os.path.join(script_dir, '%(title)s.%(ext)s')

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_template,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'nocheckcertificate': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Downloading and converting to MP3...")
            ydl.download([url])
            print("Download and conversion completed successfully.")
    except Exception as e:
        print(f"An error occurred during download or conversion: {e}")

if __name__ == "__main__":
    check_dependencies()

    video_url = input("Enter the URL of a YouTube video: ").strip()
    if not video_url:
        print("No URL entered. Exiting.")
    else:
        download_and_convert_to_mp3(video_url)
