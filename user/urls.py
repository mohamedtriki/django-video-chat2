from django.contrib import admin
from django.urls import path ,include
from django.conf.urls.static import static
from django.conf import settings
from user import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name='home'
urlpatterns = [
    path('',views.userlist,name='user'),
    path('<username>', views.user),
]
urlpatterns+= staticfiles_urlpatterns()          
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)