FROM python:3

WORKDIR /usr/src/app

COPY acf.py ./

RUN apt-get update

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install --upgrade Pillow

CMD [ "python3", "acf.py" ]
