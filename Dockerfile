FROM python:3.11-rc-alpine3.16

WORKDIR /app
RUN apk add gcc g++ 
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["python3", "main.py"]

