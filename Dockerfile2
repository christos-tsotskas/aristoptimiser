FROM python:3
MAINTAINER Christos Tsotskas <c.tsotskas@gmail.com>
COPY . /app
WORKDIR /app
RUN ls -al
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 3000

#ENTRYPOINT ["python3"]
#CMD ["aristoptimiser/web_optimiser_configuration.py"]

#CMD ["python3","aristoptimiser","web_optimiser_configuration.py"]

#RUN which python
#RUN which python3
#CMD ["python", "aristoptimiser/web_optimiser_configuration.py"]
CMD python aristoptimiser/web_optimiser_configuration.py