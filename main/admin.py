from django.contrib import admin

from main.models import News, Activity, Announcement
from main.forms import News_Admin, Activity_Admin, Announcement_Admin

# Register your models here.

admin.site.register(News, News_Admin)
admin.site.register(Activity, Activity_Admin)
admin.site.register(Announcement, Announcement_Admin)