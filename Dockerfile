FROM ubuntu:16.04


RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

EXPOSE 57777
EXPOSE 8080

WORKDIR /app
#RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]
RUN ["apt-get", "install", "-y", "netcat"]
RUN ["apt-get", "install", "-y", "curl"]

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "App.py" ]