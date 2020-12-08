from django.conf.urls import url
from .views import index, register, user_login, user_logout, fetch, content
urlpatterns = [
    url(r'^$',index,name='index'),
    url(r'index',index,name='index'),
    url(r'register', register, name='register'),
    url(r'login', user_login, name='login'),
    url(r'logout', user_logout, name='logout'),
    url(r'fetch', fetch, name='fetch'),
    #url(r'content', content, name='content'),

]