from time import sleep

from bs4 import BeautifulSoup


class ShazamChart:
    def __init__(self, url, driver):
        self.url = url
        self.driver = driver

    def parse(self):
        self.open()
        sleep(2)  # we have to explicitly wait here so javascript content is loaded

        soup = BeautifulSoup(self.driver.page_source, features='lxml')

        tracks = [
            {
                'number': int(track.select_one('.number').get_text().strip()),
                'title': track.select_one('.title').get_text().strip(),
                'artist': track.select_one('.artist').get_text().strip()
            } for track in soup.select('li.track')
        ]

        return tracks

    def open(self):
        self.driver.get(self.url)
