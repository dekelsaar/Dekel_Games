FROM python:3.8

WORKDIR /app/

COPY ./Scores.txt /app/
COPY ./*.py /app/
COPY ./templates/* /app/templates/
COPY ./Tests/* /app/Tests/

RUN pip install selenium
RUN pip install flask
RUN pip install webdriver-manager
RUN pip install CurrencyConverter

EXPOSE 5000/tcp


CMD python3 Main_Scores.py
