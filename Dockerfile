FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
# ENTRYPOINT ["python"]
CMD gunicorn --bind 0.0.0.0:$PORT wsgi
# CMD ["app.py"]
