from selenium.webdriver.common.action_chains import ActionChains


class VKPlaylist:
    def __init__(self, name, tracks, driver, vk):
        self.name = name
        self.tracks = tracks
        self.driver = driver
        self.vk = vk

    def generate(self):
        self.create()
        self.populate()

    def create(self):
        self.driver.find_element_by_css_selector(
            '.audio_page__add_playlist_btn').click()
        self.driver.find_elements_by_css_selector(
            '#ape_pl_name')[-1].send_keys(self.name)
        self.driver.find_elements_by_css_selector(
            '.ape_discover_checkbox')[-1].click()
        self.driver.find_element_by_xpath(
            '//*[contains(text(), "Save")]').click()

    def populate(self):
        for track in self.tracks:
            try:
                found_track = self.vk.search_track(track)
            except ValueError:
                continue

            self.add(found_track)

    def add(self, track):
        if 'firefox' in self.driver.capabilities['browserName']:
            scroll_to_coords = f"window.scrollTo({track.location['x']}, {track.location['y'] - 200});"
            self.driver.execute_script(scroll_to_coords)

        ActionChains(self.driver).move_to_element(track).perform()

        show_more = self.driver.find_element_by_css_selector(
            '.audio_row__actions .audio_row__action_more')
        ActionChains(self.driver).move_to_element(show_more).perform()

        add_to_playlist = self.driver.find_element_by_css_selector(
            '.audio_row__actions .audio_row__more_action_add_to_playlist')
        ActionChains(self.driver).move_to_element(add_to_playlist).perform()

        self.driver.find_element_by_xpath(
            f'//*[contains(text(), "{self.name.split(" ")[0]}") and contains(@class, "audio_row__action_playlist")]').click()
