from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Profile(models.Model):
    """ Таблица данных пользователя. Не связана с аутентификацией. """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    fathername = models.CharField(max_length=32)
    location = models.CharField(max_length=100)
    education_place = models.CharField(max_length=100, null=True)
    birth_date = models.DateField(null=True)


class Activity(models.Model):
    """ Таблица данных о мероприятиях. """
    author_id = models.IntegerField(default=-1)
    title = models.CharField(max_length=200)
    img_url = models.FileField(upload_to='activity/img/%Y/%m/')
    url = models.URLField(max_length=100)
    description = models.CharField(max_length=1000)
    program = models.CharField(max_length=1000)
    program_file = models.FileField(upload_to='activity/files/%Y/%m/')
    members = models.ManyToManyField(User)
    location = models.CharField(max_length=200)
    start_datetime = models.DateTimeField(null=True)
    end_datetime = models.DateTimeField(null=True)

    """ Системные поля """
    create_datetime = models.DateTimeField(auto_now_add=True)
    edit_datetime = models.DateTimeField(auto_now=True)
    is_end = models.BooleanField(default=False)
    is_ready = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s" % self.title


class AttendUser(models.Model):
    """ Связывает пользователей с мероприятиями. """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    activity = models.OneToOneField(Activity, on_delete=models.CASCADE)


class News(models.Model):
    """ Модель новости """
    title = models.CharField(max_length=100)
    img_url = models.FileField(upload_to='news/%Y/%m/')
    description = models.CharField(max_length=5000)
    post_datetime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s" % self.title


class Announcement(models.Model):
    """ Модель анонса мероприятий """
    title = models.CharField(max_length=100)
    img_url = models.FileField(upload_to='announcement/%Y/%m/')
    description = models.CharField(max_length=5000)
    url = models.URLField(max_length=200)
    post_datetime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s" % self.title


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """ Обновление Profile, когда создается новый User """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """ Обновление Profile, когда обновляется User """
    instance.profile.save()
