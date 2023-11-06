FROM python:3.10-slim

RUN pip install pipenv

WORKDIR /app
COPY Pipfile* ./

RUN pipenv install --system --deploy

COPY predict.py ./
COPY model.bin ./
COPY test_input.json ./

EXPOSE 80

CMD ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "80"]