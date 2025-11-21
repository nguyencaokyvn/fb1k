import os
import yt_dlp

def download_video(url, output_dir="downloads"):
    """
    Downloads a video from a given URL using yt-dlp.
    
    Args:
        url (str): The URL of the video to download.
        output_dir (str): The directory to save the downloaded video.
        
    Returns:
        str: The absolute path to the downloaded video file, or None if failed.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
        'nocheckcertificate': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video from: {url}")
            info_dict = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info_dict)
            print(f"Download complete: {filename}")
            return os.path.abspath(filename)
    except Exception as e:
        print(f"Error downloading video: {e}")
        return None

if __name__ == "__main__":
    # Test with a dummy URL or valid one if available
    pass
