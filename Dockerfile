FROM python:3.8-slim-buster

COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt


CMD ["python3", "aristoptimiser/web_optimiser_configuration.py"]