FROM python:3

WORKDIR /home/ec2-user/django_project

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python3", "manage.py", "runserver","0.0.0.0:8000" ]
