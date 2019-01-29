FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ADD requirements.txt /usr/src/app/
RUN pip install -r requirements.txt
ADD *.py /usr/src/app/
CMD ["gunicorn", "flask_app:app", "-b", "0.0.0.0:5000"]
