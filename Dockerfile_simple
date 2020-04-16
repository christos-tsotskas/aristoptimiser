FROM python:3.6-slim-buster

COPY . /app
WORKDIR /app
RUN pip install pipenv
RUN ls -al
RUN pipenv install --system --deploy --ignore-pipfile
RUN pipenv install flask



CMD ["python", "aristoptimiser/web_optimiser_configuration.py"]