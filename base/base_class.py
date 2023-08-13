import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Metod assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Page titles assert - OK")

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Finish URL - OK")