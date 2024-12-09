import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from pytube import Playlist

class YouTubeMusicBot:
    def __init__(self, proxy_list_file, number_of_tabs, music_link):
        self.proxy_list_file = self.verify_proxy_list_file(proxy_list_file)
        self.music_link = music_link
        self.number_of_tabs = number_of_tabs
        self.extension_autorefresh = "Extensions\\AutoReload.crx"
        self.extension_ublock_origin = "Extensions\\UBlockOrigin.crx"
        self.proxy_list = self.load_proxy_list()        
        # Install ChromeDriver
        chromedriver_autoinstaller.install()

    def verify_proxy_list_file(self, proxy_list_file):
        while not os.path.isfile(proxy_list_file):
            print(f"Proxy list file '{proxy_list_file}' not found.")
            proxy_list_file = input("Please enter the correct path to the proxy list file: ")
        return proxy_list_file

    def load_proxy_list(self):
        with open(self.proxy_list_file, "r") as file:
            proxy_list = file.readlines()
        return [proxy.strip() for proxy in proxy_list]

    def setup_driver(self, proxy):
        chrome_options = Options()
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        chrome_options.add_extension(self.extension_autorefresh)
        chrome_options.add_extension(self.extension_ublock_origin)
        
        # Proxy configuration
        # chrome_options.add_argument(f"--proxy-server={proxy}")
        
        return webdriver.Chrome(options=chrome_options)

    def open_tabs_audio(self, driver):
        try:
            driver.get("https://music.youtube.com/")
            time.sleep(5)
            for _ in range(1, self.number_of_tabs):
                driver.execute_script("window.open('about:blank', '_blank');")
                driver.switch_to.window(driver.window_handles[-1])
                driver.get(self.music_link)
                time.sleep(6)
        except Exception as e:
            print(f"An error occurred in open_tabs_audio: {e}")

    def open_tabs_for_playlist(self, driver, urls):
        try:
            driver.get("https://music.youtube.com/")
            time.sleep(5)
            for url in urls:
                driver.execute_script("window.open('about:blank', '_blank');")
                driver.switch_to.window(driver.window_handles[-1])
                driver.get(url)
                time.sleep(6)
        except Exception as e:
            print(f"An error occurred in open_tabs_for_playlist: {e}")

    def close_all_tabs(self, driver):
        handles = driver.window_handles
        for handle in handles[1:]:
            try:
                driver.switch_to.window(handle)
                driver.close()
            except Exception as e:
                print(f"An error occurred while closing a tab: {e}")
        driver.switch_to.window(handles[0])

    def run(self):
        while True:
            for proxy in self.proxy_list:
                driver = self.setup_driver(proxy)
                if user_choice == 1:
                    self.open_tabs_audio(driver)
                    time.sleep(20)  # 2 minutes and 38 seconds
                    self.close_all_tabs(driver)
                    driver.quit()
                    time.sleep(10)  # Adjust the wait time as needed
                elif user_choice == 2:
                    urls = self.get_playlist_urls(self.music_link)
                    self.open_tabs_for_playlist(driver, urls)
                    time.sleep(120)  # Wait for 30 minutes
                    self.close_all_tabs(driver)
                    driver.quit()
                    time.sleep(10)  # Adjust the wait time as needed

    def get_playlist_urls(self, playlist_url):
        playlist = Playlist(playlist_url)
        print('Number Of Videos In playlist: %s' % len(playlist.video_urls))
        urls = []
        for url in playlist.video_urls:
            music_url = url.replace('www.youtube.com', 'music.youtube.com')
            urls.append(music_url)
        return urls

if __name__ == "__main__":
    try:
        print("---------------Auto Streaming Youtube Music Bot-------------------")
        number_of_tabs = int(input("How many Tabs You want to Open: "))
        
        print("------------------------------------------")
        print("")
        print("(1)- For Single Audio Stream\n(2)- For Playlist Stream")
        
        user_choice = int(input("Please Enter Your Choice: "))
        if user_choice in [1, 2]:
            audio_link = input("Enter Youtube Music Link: ")
            proxy_list_file = input("Enter the path to the proxy list file: ")
            proxy_list_file = proxy_list_file.strip('"')
            bot = YouTubeMusicBot(proxy_list_file=proxy_list_file, number_of_tabs=number_of_tabs, music_link=audio_link)
            bot.run()
        else:
            print("Invalid Choice!")
    except ValueError:
        print("Please Enter Only Numbers")
