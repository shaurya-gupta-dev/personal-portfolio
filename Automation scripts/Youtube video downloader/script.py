import os
import sys
import yt_dlp

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def download(urls, output_folder='downloads'):
    create_folder(output_folder)
    
    ydl_opts = {
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'), # Safe path
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'noplaylist': False,  # Allow playlists and single videos
        'quiet': False,       # Show download progress
        'no_warnings': True,
        'ignoreerrors': True, # Don't stop on download errors
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        if isinstance(urls, list):
            ydl.download(urls)
        else:
            ydl.download([urls])

def load_urls_from_file(file_path):
    if not os.path.isfile(file_path):
        print(f"[ERROR] URL list file '{file_path}' not found.")
        sys.exit(1)

    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def main():
    print("\n🔥 YouTube Downloader Automation 🔥\n")
    choice = input("Enter '1' to download a single video\nEnter '2' to download from a URL list (urls.txt): ").strip()

    if choice == '1':
        url = input("Paste the YouTube URL: ").strip()
        if url:
            download(url)
        else:
            print("[ERROR] No URL provided.")
    elif choice == '2':
        urls = load_urls_from_file('urls.txt')
        if urls:
            download(urls)
        else:
            print("[ERROR] No URLs found in file.")
    else:
        print("[ERROR] Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
