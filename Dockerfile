FROM python:3.11.2-alpine

WORKDIR /app

ENV PORT=3000

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY run.py .

COPY app.py .

COPY data data/

COPY config.py .

COPY business_logic business_logic/

COPY presentation presentation/

EXPOSE 3000

CMD ["python", "/app/run.py"]