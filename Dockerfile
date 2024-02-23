FROM python:3.12
WORKDIR /srv
COPY . .
ENV HOST=0.0.0.0
EXPOSE 8080
CMD ["python", "-m", "app.server"]
