FROM python:3.8-slim-buster

WORKDIR /gw_info_api

COPY ./ /gw_info_api

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install -e .'[dev,test]'

EXPOSE 5001

ENTRYPOINT ["python3", "/gw_info_api/manage.py", "runserver"]
