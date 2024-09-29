FROM python:3.11.9-alpine3.20


ENV PIP_DISABLE_PIP_CHECK_VERSION 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk del build-deps \
    && apk --no-cache add linux-headers g++ gettext cmake make gettext-dev libintl




WORKDIR /home/amir/code
RUN pip install --upgrade pip
COPY ./requirements.txt . 
RUN pip install -r requirements.txt 
RUN pip list
RUN echo $PATH

COPY . .
COPY ./entrypoint.sh .


CMD ["/bin/bash", "/home/amir/code/entrypoint.sh"]
