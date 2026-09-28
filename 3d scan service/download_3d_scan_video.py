#!/usr/bin/env python3
"""
Fairlady Factory - "3D Scan Service" video downloader
======================================================
Downloads a Facebook / Instagram / YouTube video into this folder.

The tool uses `yt-dlp` (the industry-standard downloader) which knows how to
resolve Facebook Reels & page videos to their real signed CDN mp4 URL and pull
it down. This runs on YOUR machine (where outbound internet + yt-dlp work).

QUICK START (on your computer):
    # 1) install yt-dlp (pick the command for your OS)
    pip install yt-dlp            # or: brew install yt-dlp  /  winget install yt-dlp

    # 2) run this script, passing the video URL
    python3 download_3d_scan_video.py "https://www.facebook.com/3forge3D/videos/.../"

Details
-------
- Output: the two demonstration clips land directly in this folder
  ("3d scan service/"). Keeps the original quality (best mp4 available).
- Facebook Reels sometimes require login; if the download is blocked, pass your
  browser cookie file with --cookies-from-browser firefox (or chrome).
"""

import subprocess, sys, os, json

HERE = os.path.dirname(os.path.abspath(__file__))

# 3D scan / 3D-printed automotive demonstration clips to download.
# yt-dlp understands Facebook, Instagram, YouTube, TikTok, etc. — just drop URLs in.
VIDEO_URLS = [
    # --- Triforge 3D (found on their FB page) ---
    # 3D-printed automotive headlights ("faros automotrices" demo)
    "https://www.facebook.com/3forge3D/videos/faros-automotrices-fabricados-con-tecnolog%C3%ADa-3d-precisi%C3%B3n-y-dise%C3%B1o-en-cada-detal/1531753005205620/",
    # (second clip on the same page)
    "https://www.facebook.com/3forge3D/videos/1531752981567320/",

    # --- InsVision AlphaScan ---
    # Direct mp4 of the AlphaScan application/reverse-engineering demo
    "https://www.insvision3d.com/wp-content/uploads/insv/auto-media/videos-web/2a04434d4e5b400c-video.mp4",

    # --- QUICKSURFACE: reverse-engineering an automotive light lens ---
    # This is a YouTube video (id 20UmU_MiL9I) - yt-dlp handles YouTube natively.
    "https://www.youtube.com/watch?v=20UmU_MiL9I",
]

# More sources worth browsing (add their reel/video URLs to VIDEO_URLS):
# - IMEE Made (LA) 3D-scans discontinued/broken car parts to CAD:
#     YouTube: https://www.youtube.com/@IMEEMADE
#     Blog project: https://imeemade.com/blog/custom-3d-printed-lights-for-our-honda-beat

# Notes:
# - The InsVision entry above is already a direct .mp4, so yt-dlp grabs it as-is.
# - The QUICKSURFACE tutorial page embeds a YouTube video; the URL here is the
#   resolved YouTube link.
# - To add more Triforge 3D clips, page through their Facebook "videos" tab, copy
#   each reel URL, and append it to VIDEO_URLS.


def ensure_ytdlp():
    """Check yt-dlp is installed, else print install hint and exit."""
    from shutil import which
    if which("yt-dlp"):
        return "yt-dlp"
    if which("yt-dlp.exe"):
        return "yt-dlp.exe"
    # fall back to python -m
    try:
        import yt_dlp  # noqa
        return False  # means: use python -m yt_dlp
    except ImportError:
        print("yt-dlp is not installed.")
        print("Install it first, e.g.:  pip install yt-dlp   (or  brew install yt-dlp)")
        print("Then re-run this script.")
        sys.exit(1)


def run(url, idx):
    import yt_dlp
    outtmpl = os.path.join(HERE, f"3d_scan_demo_{idx:02d}_%(id)s.%(ext)s")
    opts = {
        "outtmpl": outtmpl,
        "format": "best[height<=1080]/best",
        "noplaylist": True,
        "quiet": False,
        # Facebook Reels sometimes need login cookies. Uncomment to use your browser session:
        # "cookiesfrombrowser": ("firefox",),   # or ("chrome",)
        "retries": 3,
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])


def main():
    urls = [u for u in VIDEO_URLS if u.strip()]
    if not urls:
        print("No video URLs configured. Edit VIDEO_URLS in this script.")
        sys.exit(1)
    print(f"About to download {len(urls)} video(s) into: {HERE}\n")
    for i, u in enumerate(urls, 1):
        print(f"\n--- [{i}/{len(urls)}] {u}")
        try:
            run(u, i)
        except Exception as e:
            print(f"FAILED: {e}")
    print("\nDone. Check the 3d scan service folder for your clips.")


if __name__ == "__main__":
    main()
