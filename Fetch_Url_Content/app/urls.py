from django.conf.urls import url
from .views import index, register, user_login, fetch
urlpatterns = [
    url(r'^$',index,name='index'),
    url(r'register', register, name='register'),
    url(r'login', user_login, name='login'),
    url(r'fetch', fetch, name='fetch'),
]