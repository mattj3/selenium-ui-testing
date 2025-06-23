FROM python:3.11-slim

RUN apt-get update && apt-get install -y chromium-driver chromium

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# try running without these
ENV CHROME_BIN=/usr/bin/chromium
ENV PATH="$PATH:/usr/lib/chromium"

CMD ["pytest"]
