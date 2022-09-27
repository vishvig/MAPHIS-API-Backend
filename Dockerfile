FROM python:3.8

RUN apt-get update && apt-get install -y python3-opencv

RUN useradd -ms /bin/bash maphis
RUN mkdir -p /opt/code
RUN chown maphis /opt/code

USER maphis

WORKDIR /opt/code

RUN mkdir -p assets

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python", "main.py"]
