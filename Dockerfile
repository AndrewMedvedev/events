FROM python:3.12

WORKDIR /admin

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod -R 775 /src/images && \
    chown -R 1000:1000 /src/images


VOLUME /src/images

COPY . .

EXPOSE 8080

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8181"]