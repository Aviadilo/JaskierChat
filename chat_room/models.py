from django.db import models
from django.contrib.auth.models import User
# from djoser.urls.base import User


class Room(models.Model):
    room_creator = models.ForeignKey(User, verbose_name='Создатель комнаты', on_delete=models.CASCADE)
    invited_users = models.ManyToManyField(User, verbose_name='Участники', related_name='inveted_users')
    created_date = models.DateTimeField('Дата создания', auto_now_add=True, auto_now=False)

    def __str__(self):
        return "Комната №{} пользователя {}".format(self.pk, self.room_creator)

    class Meta:
        verbose_name = 'Комната чата'
        verbose_name_plural = 'Комнаты чатов'


class Chat(models.Model):
    room = models.ForeignKey(Room, verbose_name='Комната чата', on_delete=models.CASCADE)
    user_of_chat = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    message = models.TextField('Сообщение', max_length=500)
    sending_date = models.DateTimeField('Дата отправки', auto_now_add=True, auto_now=False)

    def __str__(self):
        return "Сообщение пользователя {} от {}".format(self.user_of_chat, self.sending_date)

    class Meta:
        verbose_name = 'Сообщение чата'
        verbose_name_plural = 'Сообщения чатов'
