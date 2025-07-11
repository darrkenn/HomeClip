FROM python:3.9-alpine
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5432
CMD ["python", "app.py"]