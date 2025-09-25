FROM python:3.13.7-slim
WORKDIR /app

RUN addgroup --system app && adduser --system --group app

RUN pip install uv

COPY pyproject.toml pytest.ini README.md ./
COPY ./src ./src

RUN uv pip install --system '.[test]'

RUN chown -R app:app /app

USER app

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]