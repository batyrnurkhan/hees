FROM python:3.11.0

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# Get the Real World example app
RUN git clone https://github.com/batyrnurkhan/hees.git /hees

# Set the working directory to /drf
# NOTE: all the directives that follow in the Dockerfile will be executed in
# that directory.

WORKDIR /hees/backend

RUN ls .

# Install any needed packages specified in requirements.txt

COPY req.txt /tmp/req.txt
RUN python3 -m pip install -r /tmp/req.txt

VOLUME /hees

EXPOSE 8000

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
# CMD ["%%CMD%%"]