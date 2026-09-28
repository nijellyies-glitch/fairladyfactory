# 3D Scan Service — Demonstration Videos

This folder holds the "3D scan / 3D-printed automotive parts" demonstration clips
linked from the **Triforge 3D** Facebook page.

Source: https://www.facebook.com/3forge3D/videos/faros-automotrices-fabricados-con-tecnolog%C3%ADa-3d-precisi%C3%B3n-y-dise%C3%B1o-en-cada-detal/1531753005205620/
(Description: "Faros automotrices fabricados con tecnología 3D, precisión y diseño en cada detalle."
— 3D-printed automotive headlights, custom pieces & restorations.)

## How to download the video

Facebook serves its Reels from time-limited, signed CDN URLs — they can't be
pulled from the static HTML, and the sandbox can't fetch them directly. So you
run the bundled downloader on **your own machine** (it uses `yt-dlp`, which
resolves the real mp4 for you):

```bash
# 1) install yt-dlp (one of these)
pip install yt-dlp
#  brew install yt-dlp
#  winget install yt-dlp

# 2) run the downloader (from this folder)
python3 "download_3d_scan_video.py"
```

The video lands in this folder as `3d_scan_demo_01_<id>.mp4`.

## If Facebook blocks the download

Reels sometimes require a logged-in session. Uncomment the `cookiesfrombrowser`
line inside `download_3d_scan_video.py` and set your browser, e.g.:

```python
"cookiesfrombrowser": ("firefox",),   # or ("chrome",)
```

Then re-run. (The web content never needs to be public — your browser's cookie
grant the same access you already have logged in.)

## Adding more clips

Just add more video URLs to the `VIDEO_URLS` list at the top of
`download_3d_scan_video.py`, one per line, and re-run.
