FROM python:3.12

WORKDIR /admin

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# RUN mkdir -p /admin/images && \
#     chmod -R 775 /admin/images && \
#     chown -R 1000:1000 /admin/images

COPY . .

EXPOSE 8080

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8181"]