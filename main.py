from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Подключим движок браузера, если его нет, то сначала установим
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://localhost:8000")

assert "Congratulations" in driver.title
