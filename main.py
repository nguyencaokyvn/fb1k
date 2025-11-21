import argparse
import os
import sys
from downloader import download_video
from watermarker import add_watermark

def main():
    parser = argparse.ArgumentParser(description="Download Facebook Reels and add a watermark.")
    parser.add_argument("url", help="URL of the Facebook Reel")
    parser.add_argument("--logo", default="logo.png", help="Path to the watermark logo image (default: logo.png)")
    parser.add_argument("--output", default="downloads", help="Output directory for downloads (default: downloads)")
    parser.add_argument("--position", default="bottom_right", 
                        choices=["bottom_right", "bottom_left", "top_right", "top_left", "center"],
                        help="Position of the watermark (default: bottom_right)")
    parser.add_argument("--padding", type=int, default=20, help="Padding from the edge in pixels (default: 20)")
    
    args = parser.parse_args()
    
    # Validate logo
    if not os.path.exists(args.logo):
        print(f"Error: Logo file '{args.logo}' not found. Please provide a valid path.")
        sys.exit(1)
        
    # Step 1: Download
    print("Step 1: Downloading video...")
    video_path = download_video(args.url, args.output)
    
    if not video_path:
        print("Failed to download video.")
        sys.exit(1)
        
    # Step 2: Watermark
    print("Step 2: Adding watermark...")
    watermarked_path = add_watermark(video_path, args.logo, position=args.position, padding=args.padding)
    
    if watermarked_path:
        print(f"\nSUCCESS! Video saved to: {watermarked_path}")
    else:
        print("\nFailed to add watermark.")
        sys.exit(1)

if __name__ == "__main__":
    main()
