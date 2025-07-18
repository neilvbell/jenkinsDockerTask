# Use Python 3.7 as a base image
FROM python:3.8-slim
# Copy contents into image
WORKDIR /app
COPY . /app
# install pip dependencies from requirements file
RUN pip install --no-cache-dir -r requirements.txt
#create environment variables to store mysql root pw. Not good practice but simple for now.
ENV MYSQL_ROOT_PASSWORD="default_root"
# Expose correct port
EXPOSE 5000
# Create an entrypoint
CMD ["python", "app.py"]
