FROM python:3.10-slim-buster

WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY ./requirements.txt /backend/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt


COPY . /backend

EXPOSE 8000
CMD uvicorn app.api.fapi:app --reload --host 0.0.0.0 --port 8000 

