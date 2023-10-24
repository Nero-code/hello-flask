FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY templates/ ./templates/
COPY static/ ./static/

RUN useradd --uid 1000 api && chown -R api /app
USER api

EXPOSE 5000
CMD ["gunicorn", "--bind=0.0.0.0:5000", "--log-level=info", "service:app"]
