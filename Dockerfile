FROM python

WORKDIR /usr/src/app

RUN pip install --no-cache-dir natsort

COPY . .

CMD [ "python", "./main.py" ]