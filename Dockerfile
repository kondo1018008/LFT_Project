FROM python:3
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/