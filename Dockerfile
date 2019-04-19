FROM python:latest
WORKDIR /home
COPY . .
RUN alias pip=pip3
RUN alias python=python3
RUN pip3 install psycopg2
RUN pip3 install Django
CMD tail -f /dev/null