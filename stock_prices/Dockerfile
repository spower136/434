FROM python:3.7
COPY . /
RUN pip3 install -r requirements.txt
CMD gunicorn -b 0.0.0.0:80 webapp:server