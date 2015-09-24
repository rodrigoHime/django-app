# django-app 
### Instalar dependências
    pip install -r requirements.txt
### Base de dados
    CREATE SCHEMA `django_app`; 
    python manage.py migrate
### RabbitMQ
RabbitMQ é um servidor de menssagens para rodas das tarefas agendadas no Celery.
#### Instalação
    sudo apt-get install rabbitmq-server
    sudo /usr/lib/rabbitmq/lib/rabbitmq-server-3.2.3/sbin/rabbitmq-plugins enable rabbitmq_management   
    sudo service rabbitmq-server restart
### Iniciar o CronJob no Celery
    python manage.py celeryd -B