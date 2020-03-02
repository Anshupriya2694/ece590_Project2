FROM python:3

MAINTAINER Your Name "anshupriya.srivastava@duke.edu"

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "dice.py" ]
