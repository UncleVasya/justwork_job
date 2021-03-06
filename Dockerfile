FROM python:3.8-slim-bullseye as base

# ----- builder -----
FROM base as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install package dependenices
RUN apt-get update && apt-get install --no-install-recommends -y \
  libpq-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

RUN pip install -r requirements.txt


# ----- final -----
FROM base

# netcat to check for postgres readiness
RUN apt-get update && apt-get install --no-install-recommends -y \
  netcat

# copy dependencies
COPY --from=builder /usr/src/app/wheels /wheels
RUN pip install --no-cache /wheels/*

# copy project
COPY . .

# run entrypoint.sh
RUN chmod +x entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]