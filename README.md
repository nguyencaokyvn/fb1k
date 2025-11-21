# Hướng dẫn sử dụng Tool Tải & Đóng Dấu Video Facebook

Tool này giúp bạn tự động tải video từ Facebook Reel và gắn logo watermark vào góc dưới bên phải.

## Yêu cầu hệ thống
1.  **Python**: Đã cài đặt Python 3.
2.  **FFmpeg**: Đã cài đặt FFmpeg và có thể chạy từ dòng lệnh (terminal).

## Cài đặt
Mở terminal tại thư mục dự án và chạy lệnh sau để cài đặt các thư viện cần thiết:

```bash
pip install -r requirements.txt
```

## Cách sử dụng
Chạy file `main.py` kèm theo đường link video Facebook Reel bạn muốn tải:

```bash
python3 main.py <LINK_FACEBOOK_REEL>
```

### Các tùy chọn nâng cao
Bạn có thể tùy chỉnh logo và thư mục lưu bằng các tham số sau:

- `--logo <đường_dẫn_ảnh>`: Đường dẫn đến file ảnh logo (mặc định là `logo.png`).
- `--output <tên_thư_mục>`: Thư mục để lưu video tải về (mặc định là `downloads`).
- `--position <vị_trí>`: Vị trí logo. Các giá trị: `bottom_right` (mặc định), `bottom_left`, `top_right`, `top_left`, `center`.
- `--padding <số_pixel>`: Khoảng cách từ lề (mặc định là 20).

### Ví dụ lệnh đầy đủ
```bash
python3 main.py "https://www.facebook.com/reel/1396021195866747" --logo my_logo.png --output video_da_tai --position top_right --padding 50
```

### Chạy riêng chức năng đóng dấu (Watermark)
Nếu bạn đã có sẵn video và chỉ muốn đóng dấu logo, hãy chạy lệnh sau:

```bash
python3 watermarker.py <đường_dẫn_video> <đường_dẫn_logo>
```

Ví dụ:
```bash
python3 watermarker.py video.mp4 logo.png
```
Bạn cũng có thể chỉ định tên file đầu ra bằng tùy chọn `--output`:
```bash
python3 watermarker.py downloads/123.mp4 logo.png --output downloads/123_logo.mp4
```

## Giải thích các file
- **main.py**: File chính để chạy chương trình. Nó kết hợp việc tải và đóng dấu.
- **downloader.py**: Chứa code dùng `yt-dlp` để tải video từ Facebook.
- **watermarker.py**: Chứa code dùng `ffmpeg` để gắn logo vào video.
- **requirements.txt**: Danh sách các thư viện Python cần cài đặt.
