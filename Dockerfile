FROM python:3.10
EXPOSE 5000

COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt

CMD python app.py
