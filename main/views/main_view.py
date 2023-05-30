from main.SiteTools.texttool import get_context
from main.models import News, Announcement
from main.SiteTools import texttool, imgtool, usertool
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.utils import dateformat

def index_page(request):
    """ Главная страница """
    context = get_context(request, "Главная", False)
    template_path = 'pages/index.html'
    context['news'] = News.objects.order_by("-id").all()[:10]
    imgtool.check_media(context['news'])
    context['announcements'] = Announcement.objects.order_by("-id").all()[:10]
    return render(request, template_path, context)

def about_page(request):
    """ Страница информации о сайте """
    context = get_context(request, "О проекте")
    template_path = 'pages/about.html'
    return render(request, template_path, context)

@login_required
def profile_page(request):
    """ Страница профиля """
    context = get_context(request, "Профиль")
    user = usertool.get_current_user(request.user.username)
    profile = user.profile
    context['email'] = user.email
    context['place_edu'] = profile.education_place
    context['birthday'] = profile.birth_date
    context['full_name'] = "{} {} {}".format(profile.surname, profile.name, profile.fathername)
    template_path = 'pages/profile_yashka.html'
    return render(request, template_path, context)


