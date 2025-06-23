import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

# Load local .env file (only works locally, not in CI)
load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://www.saucedemo.com")

@pytest.fixture(scope="session")
def username():
    return os.getenv("UI_USERNAME")

@pytest.fixture(scope="session")
def password():
    return os.getenv("UI_PASSWORD")

@pytest.fixture
def driver():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
