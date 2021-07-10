from time import sleep


class VK:
    @staticmethod
    def generate_track_search_query(track):
        search_query = f"{track['title']} {track['artist']}"
        return search_query

    def __init__(self, vk_user, vk_password, driver):
        self.vk_user = vk_user
        self.vk_password = vk_password
        self.driver = driver

    def open(self):
        self.driver.get('https://vk.com')

    def login(self):
        self.open()

        self.driver.find_element_by_css_selector(
            '#index_email').send_keys(self.vk_user)
        self.driver.find_element_by_css_selector(
            '#index_pass').send_keys(self.vk_password)
        self.driver.find_element_by_css_selector('#index_login_button').click()

    def open_music(self):
        self.login()

        self.driver.find_element_by_css_selector('#l_aud').click()

    def search_track(self, track):
        search_query = VK.generate_track_search_query(track)
        search = self.driver.find_element_by_css_selector('#audio_search')
        search.clear()
        search.send_keys(search_query)
        # we have to explicitily wait here so that specific search content pops up
        sleep(2)

        track_blocks = self.driver.find_elements_by_css_selector(
            '.audio_page__audio_list_block')
        if len(track_blocks) == 1:
            raise ValueError('Song not found.')
        found_track = track_blocks[-1].find_element_by_css_selector(
            '.audio_row.audio_can_add')
        return found_track
