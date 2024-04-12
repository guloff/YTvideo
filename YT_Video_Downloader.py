import os
import yt_dlp

def list_formats(url):
    try:
        with yt_dlp.YoutubeDL() as ydl:
            meta = ydl.extract_info(url, download=False)
            if 'formats' in meta:
                print("Available formats:")
                for f in meta['formats']:
                    print(f"Format code: {f['format_id']}, Extension: {f['ext']}, "
                          f"Resolution: {f.get('resolution', 'audio only')}, "
                          f"Bitrate: {f.get('abr', 'N/A')} kbps, "
                          f"FPS: {f.get('fps', 'N/A')}, "
                          f"Video codec: {f.get('vcodec', 'N/A')}, "
                          f"Audio codec: {f.get('acodec', 'N/A')}, "
                          f"Note: {f.get('format_note', '')}")
            else:
                print("No formats found. This might be an audio-only item.")
    except Exception as e:
        print(f"An error occurred: {e}")

def download_video(url, format_codes):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    for format_code in format_codes:
        ydl_opts = {
            'format': format_code,
            'outtmpl': os.path.join(script_dir, '%(title)s-%(format_id)s.%(ext)s'),
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                print(f"Download completed successfully for format code: {format_code}.")
        except Exception as e:
            print(f"Failed to download for format code {format_code}: {e}")

if __name__ == "__main__":
    video_url = input("Enter the URL of a YouTube video: ")
    if not video_url.strip():
        print("No URL entered. Exiting.")
    else:
        list_formats(video_url)
        format_codes_input = input("Enter two desired format codes to download the video (e.g., '22,18'): ")
        format_codes = [code.strip() for code in format_codes_input.split(',')]
        if not format_codes or len(format_codes) < 2:
            print("Insufficient format codes entered. Exiting.")
        else:
            download_video(video_url, format_codes)
