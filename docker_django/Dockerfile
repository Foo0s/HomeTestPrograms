FROM python:3.7-alpine3.12
RUN apk add --no-cache tini
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /apps
RUN apk --update add
RUN apk add gcc libc-dev libffi-dev jpeg-dev zlib-dev libjpeg
RUN apk add postgresql-dev
RUN pip install --upgrade pip
COPY ./requirements.txt .
COPY ./entrypoint.sh .
RUN chmod +x entrypoint.sh
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["/app/entrypoint.sh"]