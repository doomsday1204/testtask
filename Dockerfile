FROM python:3.8

COPY req.txt .
RUN pip install -r req.txt

COPY . .

CMD ["python", "app.py"]