FROM python:3.12-slim

RUN useradd --create-home --shell /usr/sbin/nologin workshop
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chmod +x /app/workshop/*.sh \
    && python init_db.py \
    && chown -R workshop:workshop /app

USER workshop
EXPOSE 8080
CMD ["python", "app.py"]
