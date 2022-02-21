FROM python:3.8

# Copy files
COPY ./requirements.txt ./

# Copy folders
COPY ./src ./src

# Install packages
RUN pip install -r requirements.txt

# Run flask app
WORKDIR /src
EXPOSE 5000
ENV FLASK_APP="api/app" FLASK_ENV=docker
CMD ["flask", "run", "-h", "0.0.0.0"]