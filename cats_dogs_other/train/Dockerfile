FROM python:3.11-slim

ARG MLFLOW_S3_ENDPOINT_URL
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY

ENV MLFLOW_S3_ENDPOINT_URL=${MLFLOW_S3_ENDPOINT_URL}
ENV AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
ENV AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}

COPY cats_dogs_other/train ./cats_dogs_other/train
COPY cats_dogs_other/requirements.txt ./cats_dogs_other/requirements.txt
COPY packages ./packages
COPY init_packages.sh ./init_packages.sh

RUN chmod -R 777 ./cats_dogs_other
RUN chmod -R 777 init_packages.sh
RUN ./init_packages.sh
RUN pip install -r /cats_dogs_other/requirements.txt