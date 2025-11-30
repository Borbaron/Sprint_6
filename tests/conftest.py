import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


from curl import *
#from data import Credentials
#from pages.auth_page import AuthPage
#from pages.main_page import MainPage


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get(main_site)
    yield driver
    driver.quit()

