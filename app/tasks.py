import datetime
import json
from random import randint
import urllib2
from celery.task import periodic_task
from app.models import Entry


@periodic_task(run_every=datetime.timedelta(minutes=2))
def get_entry():
    for i in range(1000):
        response = urllib2.urlopen('http://namey.muffinlabs.com/name.json')
        name = json.load(response)[0]
        number = randint(100, 9999)
        Entry.objects.create(text=name, number=number)
