# Use the official lightweight Python image
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Copy project files to container
COPY . /app

# Install pip requirements
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose Streamlit default port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
