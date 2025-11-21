# FB1K - Facebook Reels Scraper & Downloader

This project provides tools to scrape Facebook Reels links from channels/profiles and download them with optional watermarking.

## Features

- **Scrape All Reels**: Extract all video links from a Facebook Reels tab (infinite scrolling supported).
- **Download & Watermark**: Download individual reels and add a custom logo watermark.
- **Lightweight**: Uses Python scripts with minimal dependencies.

## Prerequisites

- **Python 3.x**
- **Google Chrome** (for scraping links)
- **FFmpeg** (for watermarking)
    - *Mac*: `brew install ffmpeg`
    - *Windows*: Download and add to PATH.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/nguyencaokyvn/fb1k.git
    cd fb1k
    ```

2.  Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Scrape All Reels Links

Use `get_all_fb_reels.py` to get a list of all video URLs from a channel.

```bash
python3 get_all_fb_reels.py "https://www.facebook.com/YOUR_CHANNEL/reels"
```

- **How it works**: Opens a Chrome browser, automatically scrolls down to load all content, and saves the links.
- **Output**: `downloads/reels_links/reels_links_<channel_name>.txt`

### 2. Download & Watermark a Single Reel

Use `main.py` to download a video and add a logo.

```bash
python3 main.py "https://www.facebook.com/reel/123456789" --logo logo.png --position bottom_right
```

- **Arguments**:
    - `url`: Facebook Reel URL.
    - `--logo`: Path to your logo image (default: `logo.png`).
    - `--position`: `bottom_right`, `bottom_left`, `top_right`, `top_left`, `center` (default: `bottom_right`).
    - `--padding`: Padding from edge in pixels (default: 20).
- **Output**: Saved in `downloads/` folder.

## Scripts Overview

| Script | Description |
| :--- | :--- |
| `get_all_fb_reels.py` | **Recommended**. Uses Selenium to scrape *all* links from a channel. |
| `main.py` | Main entry point for downloading and watermarking a single video. |
| `downloader.py` | Helper module to download videos using `yt-dlp`. |
| `watermarker.py` | Helper module to add watermarks using `ffmpeg`. |
| `get_fb_reels.py` | Legacy script using `yt-dlp` for scraping (less reliable for full channels). |

## Troubleshooting

- **Scraping stops early**: Check your internet connection. The script stops if no new content loads after 5 scroll attempts.
- **Browser closes immediately**: Ensure Chrome is installed. The script manages the driver automatically.
- **Watermark fails**: Ensure `ffmpeg` is installed and accessible in your terminal.
