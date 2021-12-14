FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY app app