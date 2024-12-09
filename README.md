# YouTube Music Watchtime Increaser and Mass Viewer

## Description
This Python bot automates the process of increasing watch time for YouTube Music by opening multiple tabs with different proxy configurations. It can stream a single audio track or an entire playlist on YouTube Music. The bot also uses Chrome extensions for auto-refresh and ad-blocking.

## Features
- Stream single audio or playlists on YouTube Music.
- Open multiple tabs for concurrent streaming.
- Support for proxy rotation using a proxy list file.
- Auto-refresh and ad-blocking via Chrome extensions.
- Automatic detection and use of ChromeDriver.

## Requirements
- Python 3.7 or higher
- Required Python libraries:
  - `selenium`
  - `chromedriver_autoinstaller`
  - `pytube`
- Google Chrome installed

## Setup
1. Install the required Python libraries:
   ```bash
   pip install selenium chromedriver-autoinstaller pytube
   ```

2. Place the required Chrome extensions in the `Extensions` folder:
   - AutoReload.crx
   - UBlockOrigin.crx

3. Prepare a proxy list file containing one proxy per line in the format:
   ```
   proxy_ip:port
   ```

## Usage
1. Run the script:
   ```bash
   python youtube_music_bot.py
   ```

2. Follow the prompts:
   - Enter the number of tabs you want to open.
   - Choose between streaming a single audio track or a playlist:
     - (1) Single Audio Stream
     - (2) Playlist Stream
   - Provide the YouTube Music link.
   - Enter the path to the proxy list file.

3. The bot will automate the streaming process.

## Options
### Single Audio Stream
- Opens multiple tabs playing the same audio track on YouTube Music.

### Playlist Stream
- Plays all videos in a playlist, replacing the `www.youtube.com` domain with `music.youtube.com` for compatibility.

## How It Works
1. **Proxy Setup**: The bot reads proxies from the provided file and configures Chrome to use them.
2. **Tabs Management**: Opens the specified number of tabs and navigates to the provided YouTube Music link or playlist.
3. **Extensions**: Uses AutoReload for periodic refreshing and UBlock Origin for ad-blocking.
4. **Playlist Support**: Converts playlist URLs for compatibility with YouTube Music.

## Notes
- Ensure that the Chrome extensions (AutoReload and UBlock Origin) are valid `.crx` files.
- The bot uses `chromedriver_autoinstaller` to ensure the correct version of ChromeDriver is installed automatically.

## Future Improvements
- Add support for dynamic proxy rotation during runtime.
- Implement advanced error handling and logging.
- Add a graphical user interface (GUI) for easier configuration.

## Disclaimer
This tool is for educational purposes only. Use it responsibly and ensure compliance with YouTube’s terms of service.

