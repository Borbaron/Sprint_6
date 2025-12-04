import pytest
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


from curl import *


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.get(main_site)
    yield driver
    driver.quit()

