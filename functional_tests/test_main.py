import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestMainPage(unittest.TestCase):
    """Тест посещения главной страницы"""

    def setUp(self):
        """"""
        # Подключим движок браузера, если его нет, то сначала установим
        self.service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=self.service)

    def tearDown(self):
        """"""
        self.browser.quit()

    def test_can_start_list_and_retrive_it_later(self):
        """"""
        self.browser.get("http://localhost:8000")

        self.assertIn("To-Do", self.browser.title)
        self.fail("Закончить тест")


if __name__ == "__main__":
    unittest.main(warnings="ignore")
