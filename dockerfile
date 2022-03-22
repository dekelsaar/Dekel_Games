FROM python:python3.8-alpine
WORKDIR /app/
COPY ./Scores.txt /app/
COPY ./*.py /app/
COPY ./Templates/* /app/Templates/
COPY ./Tests/* /app/Tests/
EXPOSE 5001
CMD python3 Main_Game.py
