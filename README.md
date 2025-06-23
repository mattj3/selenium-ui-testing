# Selenium UI Automation with Python + Docker + GitHub Actions

## Overview

This project demonstrates a Selenium-based UI test framework for [saucedemo.com](https://www.saucedemo.com) using:

- Python + Selenium + Pytest
- Headless Chrome browser
- Dockerized environment for tests
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
├── Dockerfile
├── .github/
│ └── workflows/tests.yml
├── README.md
└── .env (local)
```

## Setup & Run Locally

1. Install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

2. Run tests:

```bash
pytest
```

3. View report:

Open reports/report.html in your browser.

## Run with Docker

```bash
docker build -t selenium-ui .
docker run selenium-ui
```
