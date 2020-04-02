FROM python:3.7-alpine3.10
COPY . /app
WORKDIR /app
RUN pip install --user -r requirements.txt
EXPOSE 5000
CMD python ./app/index.py
