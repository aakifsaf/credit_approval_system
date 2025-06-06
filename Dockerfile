FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app

CMD ["./wait_for_db.sh","gunicorn", "credit_approval_system.wsgi:application", "--bind", "0.0.0.0:8000"]