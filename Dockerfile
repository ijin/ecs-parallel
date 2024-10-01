FROM python:3-slim
EXPOSE 8080
CMD ["/bin/sh", "-c", "touch alive; echo hi > index.html; python -m http.server 8080"]
