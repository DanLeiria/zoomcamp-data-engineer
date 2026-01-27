# Start with slim Python 3.12 image
FROM python:3.12.12-slim

# Install Poetry
RUN pip install --no-cache-dir poetry

# Set working directory
WORKDIR /code

# Configure Poetry to create virtual environment in project directory
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

# Add virtual environment to PATH so we can use installed packages
ENV PATH="/code/.venv/bin:$PATH"

# Copy dependency files first (better layer caching)
COPY pyproject.toml poetry.lock ./
# Install dependencies from lock file (ensures reproducible builds)
RUN poetry install --no-root --only main

# Copy application code
COPY ingestion.py .

# Copy data directory
COPY data ./data

# Set entry point
ENTRYPOINT ["poetry", "run", "python", "ingestion.py"]