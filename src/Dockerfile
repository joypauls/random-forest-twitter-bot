FROM python:3.9

RUN apt-get update && apt-get install -y cron

WORKDIR /usr/src/app

# build context is src
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "app.py" ]