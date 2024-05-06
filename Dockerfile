FROM python:3.12.2

WORKDIR /cs333-final-project

COPY . /cs333-final-project

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED 1

CMD ["python", "main.py"]