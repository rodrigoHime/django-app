# coding=utf-8
from django.dispatch import receiver
from django.db import models
from django.db.models.signals import post_save, post_delete
from datetime import datetime


class Entry(models.Model):
    number = models.IntegerField(u'Número')
    text = models.CharField(u'Texto', max_length=255, db_index=True)


class Log(models.Model):
    TYPES = (
        (1, 'Criação'),
        (2, 'Atualização'),
        (3, 'Deleção'),
    )
    text = models.CharField('Log', max_length=255)
    type = models.IntegerField(choices=TYPES, default=1)
    datetime = models.DateTimeField('Data de Criação', default=datetime.now)

    def get_str_type(self):
        return dict(self.TYPES)[self.type]


@receiver(post_save, sender=Entry)
def post_save_entry(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Log.objects.create(text='Entrada número "%s" cadastrada' % instance.number, type=1)
    else:
        Log.objects.create(text='Entrada número "%s" atualizadaa' % instance.number, type=2)


@receiver(post_delete, sender=Entry)
def post_delete_entry(sender, instance, **kwargs):
    Log.objects.create(text='Entrada de número "%s" removida' % instance.number, type=3)


