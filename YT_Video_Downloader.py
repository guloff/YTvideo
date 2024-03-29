import os
import yt_dlp

def list_formats(url):
    with yt_dlp.YoutubeDL() as ydl:
        meta = ydl.extract_info(url, download=False)
        if 'formats' in meta:
            for f in meta['formats']:
                print(f"format code: {f['format_id']}, extension: {f['ext']}, resolution: {f.get('resolution', 'audio only')}, note: {f.get('format_note', '')}")

def download_video(url, format_code):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ydl_opts = {
        'format': format_code,
        'outtmpl': os.path.join(script_dir, '%(title)s-%(format_id)s.%(ext)s'),
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Give me a link to a YouTube video: ")
    print("Available Formats:")
    list_formats(video_url)
    
    format_code = input("Enter the desired format code to download the video (for instance, '22'): ")
    download_video(video_url, format_code)
