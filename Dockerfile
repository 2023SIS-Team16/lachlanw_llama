FROM ubuntu:22.04

WORKDIR /python-docker

RUN apt-get update && apt-get install -y python3 python3-pip cmake wget build-essential

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]