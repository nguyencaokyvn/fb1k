import os
import subprocess

def add_watermark(video_path, logo_path, output_path=None, position="bottom_right", padding=20):
    """
    Adds a watermark to a video using ffmpeg.
    
    Args:
        video_path (str): Path to the input video.
        logo_path (str): Path to the logo image.
        output_path (str): Path to save the watermarked video.
        position (str): Position of the watermark. 
                        Values: "bottom_right" (default), "bottom_left", "top_right", "top_left", "center".
        padding (int): Padding in pixels from the edge (default: 20).
        
    Returns:
        str: Path to the watermarked video, or None if failed.
    """
    if not os.path.exists(video_path):
        print(f"Error: Video file not found at {video_path}")
        return None
        
    if not os.path.exists(logo_path):
        print(f"Error: Logo file not found at {logo_path}")
        return None
        
    if output_path is None:
        base, ext = os.path.splitext(video_path)
        output_path = f"{base}_watermarked{ext}"
        
    # Define overlay coordinates based on position
    # We use the padding variable in the ffmpeg expression
    overlay_map = {
        "bottom_right": f"overlay=W-w-{padding}:H-h-{padding}",
        "bottom_left": f"overlay={padding}:H-h-{padding}",
        "top_right": f"overlay=W-w-{padding}:{padding}",
        "top_left": f"overlay={padding}:{padding}",
        "center": "overlay=(W-w)/2:(H-h)/2"
    }
    
    overlay_cmd = overlay_map.get(position, overlay_map["bottom_right"])
        
    cmd = [
        'ffmpeg',
        '-i', video_path,
        '-i', logo_path,
        '-filter_complex', overlay_cmd,
        '-codec:a', 'copy',
        '-y', # Overwrite output file if it exists
        output_path
    ]
    
    try:
        print(f"Adding watermark to {video_path}...")
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Watermarking complete: {output_path}")
        return output_path
    except subprocess.CalledProcessError as e:
        print(f"Error adding watermark: {e}")
        # print(e.stderr.decode()) # Uncomment for debugging
        return None

if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="Add a watermark to a video.")
    parser.add_argument("video_path", help="Path to the input video")
    parser.add_argument("logo_path", help="Path to the logo image")
    parser.add_argument("--output", help="Path to save the watermarked video (optional)")
    parser.add_argument("--position", default="bottom_right", 
                        choices=["bottom_right", "bottom_left", "top_right", "top_left", "center"],
                        help="Position of the watermark (default: bottom_right)")
    parser.add_argument("--padding", type=int, default=20, help="Padding from the edge in pixels (default: 20)")

    args = parser.parse_args()

    result = add_watermark(args.video_path, args.logo_path, args.output, args.position, args.padding)
    
    if result:
        print(f"Success! Saved to: {result}")
    else:
        sys.exit(1)
