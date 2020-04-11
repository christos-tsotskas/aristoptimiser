FROM python:3
MAINTAINER Christos Tsotskas <c.tsotskas@gmail.com>
COPY . /app
WORKDIR /app
RUN ls -al
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["aristoptimiser/web_optimiser_configuration.py"]