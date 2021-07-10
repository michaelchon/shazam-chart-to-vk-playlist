from selenium import webdriver

from config import config
from utils.shazam_chart import ShazamChart
from utils.vk import VK
from utils.vk_playlist import VKPlaylist


def main():
    options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(10)

    shazam_chart = ShazamChart(config['chart']['url'], driver)
    tracks = shazam_chart.parse()

    prepared_tracks = sorted(tracks, key=lambda track: track['number'])
    prepared_tracks = prepared_tracks[
        config['chart']['start'] - 1:
        config['chart']['end']
    ]
    prepared_tracks.reverse()

    vk = VK(config['vk']['user'], config['vk']['password'], driver)
    vk.open_music()

    vk_playlist = VKPlaylist(
        config['vk']['playlist'], prepared_tracks, driver, vk)
    vk_playlist.generate()

    driver.quit()


if __name__ == '__main__':
    main()
