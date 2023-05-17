FROM python:3.10-slim as base

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV APPDIR=/opt/app
WORKDIR $APPDIR


FROM base as poetry

ENV POETRY_VERSION=1.3.1
ENV POETRY_HOME=/opt/poetry
ENV PATH="$POETRY_HOME/bin:$PATH"

RUN apt-get update &&  apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -


FROM poetry as requirements-builder

COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt -o requirements.txt


FROM base as production

COPY --from=requirements-builder $APPDIR/requirements.txt .
RUN pip install --require-hashes --no-cache-dir -r requirements.txt
COPY . .

CMD bash -c "alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 3402 --log-level info"


FROM poetry as development
RUN apt update && apt install -y --no-install-recommends git
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && \
    poetry install
COPY . .
