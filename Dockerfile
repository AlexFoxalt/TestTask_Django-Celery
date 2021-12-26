FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt update

RUN mkdir /CSVFaker
RUN mkdir /CSVFaker/accounts
RUN mkdir /CSVFaker/base
RUN mkdir /CSVFaker/commands
RUN mkdir /CSVFaker/CSVFaker
RUN mkdir /CSVFaker/services

WORKDIR /CSVFaker

COPY ./accounts ./accounts
COPY ./base ./base
COPY ./commands ./commands
COPY ./CSVFaker ./CSVFaker
COPY ./services ./services
COPY ./manage.py ./manage.py
COPY ./requirements.txt ./requirements.txt


RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["bash"]