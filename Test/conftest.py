import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="C:/auto_test/chromedriver_win32/chromedriver.exe")
    yield driver
    driver.quit()