import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

# Load local .env file (only works locally, not in CI)
load_dotenv()

REQUIRED_ENV_VARS = ["UI_USERNAME", "UI_PASSWORD"]

# Fail fast if required env vars are missing
for var in REQUIRED_ENV_VARS:
    if not os.getenv(var):
        raise RuntimeError(f"Required environment variable '{var}' is missing.")

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
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
