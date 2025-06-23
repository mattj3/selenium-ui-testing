# Selenium UI Automation with Python + Pytest + GitHub Actions

## Overview

This project demonstrates a Selenium-based UI test framework for [saucedemo.com](https://www.saucedemo.com) using:

- Python + Selenium + Pytest
- Headless Chrome browser
- GitHub Actions CI pipeline
- HTML test reports

## Folder Structure

```
selenium-ui-testing/
│
├── tests/
│ ├── test_login.py
│ └── conftest.py
│
├── pages/
│ └── login_page.py
│
├── reports/
│ └── (generated test reports)
│
├── requirements.txt
├── pytest.ini
├── .github/
│ └── workflows/tests.yml
├── README.md
└── .env (local)
```

## Setup and Run Locally

1. Clone repo:

```bash
git clone https://github.com/yourusername/selenium-ui-testing.git
cd selenium-ui-testing
```

2. Create and activate virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create .env file for local environment variables (in project root):

```env
UI_USERNAME=your_username
UI_PASSWORD=your_password
```

5. Run tests (locally):

```bash
pytest
```

6. View report:

Open `reports/report.html` in your browser.

## GitHub Actions

This project is configured with a GitHub Actions workflow that runs your Selenium tests automatically on push and pull requests.

Secrets required: `UI_USERNAME` and `UI_PASSWORD` must be configured in your repository settings under Settings > Secrets and variables > Actions > Repository secrets.

The workflow uses a Linux runner with Chrome pre-installed, and Selenium manages ChromeDriver automatically.
