FROM python:latest

ADD main.py .

RUN pip install requests beautifulsoup4

CMD [ "python", "./main.py"]
