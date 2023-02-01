FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/

COPY req.txt .

RUN pip install -r req.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "shortener_app/main.py"]
