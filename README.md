# Django_Blog_Post

Commands to run the application:

--> yum install update

--> Hostnamectl set-hostname django-server

--> Modify /etc/hosts file to add entry for IP address ---> Django-server



For SSH Key Based Authentication:

--> mkdir -p ~/.ssh

--> ssh-keygen -b 4096 -t rsa -m pem

--> scp ~/.ssh/id_rsa.pub lakshman@IP:~/.ssh/authorized_keys

--> chmod 700 ~/.ssh/

--> chmod 600 ~/.ssh/*

--> nano /etc/ssh/sshd_config —> PasswordAuthentication no, PermitRootLogin no

--> systemctl restart ssh



Installing Dependencises and running Application:

 --> apt-get install python3-pip
 
 --> apt-get install python3-venv
 
 --> python3 -m venv Django_project/venv
 
 --> cd Django-project —> source venv/bin/activate
 
 --> pip install -r requirements.txt



Modify project settings.py file ALLOWED_HOSTS to include server IP address so that Django knows whom to allow

Inside settings.py file

 --> STATIC_ROOT = os.path.join(BASE_DIR, ’static’)

python manage.py collectstatic



Lastly run the application using the command below:

--> python manage.py runserver 0.0.0.0:8000

Then from navigating to serverpublicIp:8000 you can view the application running.



Functionalities:

--> Implemented back end database for storing users and there Posts

--> Different Users can login and add there Posts

--> Users can request password reset through email if they forgot password

--> Followed security best practices to use host header validation and to securely store secrets





