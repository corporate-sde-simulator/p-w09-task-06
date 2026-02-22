FROM python:latest

# Consider multi-stage build: builder stage for deps, runtime stage for app

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN pip install pytest flake8 mypy  # Dev tools don't belong in prod!

# Should add: RUN useradd -m appuser && USER appuser

EXPOSE 8080

# Should add: HEALTHCHECK CMD curl -f http://localhost:8080/health || exit 1

CMD ["python", "app.py"]
