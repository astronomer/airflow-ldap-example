ARG AIRFLOW_IMAGE

FROM $AIRFLOW_IMAGE

COPY packages.txt .
USER root
RUN if [[ -s packages.txt ]]; then \
        apt-get update -y && cat packages.txt | xargs apt-get install -y --no-install-recommends \
        && apt-get autoremove -yqq --purge \
        && rm -rf /var/lib/apt/lists/*; \
    fi

COPY requirements.txt .
USER airflow
RUN pip install --no-cache-dir --user -q -r requirements.txt

COPY webserver_config.py .

