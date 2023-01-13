FROM python:3.9-slim

WORKDIR /python-docker

RUN pip3 install flask
RUN pip3 install flask-mysql

COPY . .

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]