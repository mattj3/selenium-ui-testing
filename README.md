# Selenium UI Automation with Python + Pytest + GitHub Actions

![Selenium Tests](https://github.com/mattj3/selenium-ui-testing/actions/workflows/ci.yml/badge.svg)

A Selenium-based UI test framework for [saucedemo.com](https://www.saucedemo.com) using:

- Python + Selenium + Pytest
- Headless Chrome browser
- GitHub Actions CI pipeline
- HTML test reports

## Folder Structure

```
selenium-ui-testing/
│
├── .github/
│ └── workflows/tests.yml
│
├── pages/
│ └── login_page.py
│
├── reports/
│ └── (generated test reports)
│
├── tests/
│ ├── test_login.py
│ └── conftest.py
│
├── .env
├── .gitignore
├── pytest.ini
├── README.md
└── requirements.txt
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

<img width="1430" alt="Screenshot 2025-06-23 at 3 04 41 PM" src="https://github.com/user-attachments/assets/f8e7c108-a7fb-4bc7-a612-98138f87d4e2" />

## GitHub Actions

This project is configured with a GitHub Actions workflow that runs your Selenium tests automatically on push and pull requests.

Secrets required: `UI_USERNAME` and `UI_PASSWORD` must be configured in your repository settings under Settings -> Secrets and variables -> Actions -> Repository secrets.

The workflow uses a Linux runner with Chrome pre-installed, and Selenium manages ChromeDriver automatically.
