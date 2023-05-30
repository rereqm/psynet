from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from it_community import settings
from main.views import main_view, registration_view, news_view, activity_view
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', registration_view.login_page),
    path('logout/', registration_view.logout_view),
    path('registration/', registration_view.registration_page),

    path('', main_view.index_page),
    path('about/', main_view.about_page),
    path('profile/', main_view.profile_page),

    path('news/', news_view.news_page),
    path('news/<int:article_id>', news_view.article_page),
    path('announcement/<int:id>', news_view.announcement_page),

    path('activity/', activity_view.main_activity_page),
    path('activity_create/', activity_view.activity_create_page),
    path('activity_edit/<int:id>', activity_view.activity_edit_page),
    path('activity/<int:activity_id>', activity_view.activity_page),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
