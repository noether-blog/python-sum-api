From python:3.12-rc-alpine3.18

RUN addgroup -S noether && adduser -S emmy -G noether

USER emmy

RUN mkdir /home/emmy/app

WORKDIR /home/emmy/app

COPY app.py app.py
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENV PATH="$PATH:/home/emmy/.local/bin"

ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "--port=8080"]

