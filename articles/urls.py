from django.conf.urls import url
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *


urlpatterns = [
    url(r'^index$',index),
    url(r'^home$',home),
    # url(r'^login_home.html$',login_home),
    url(r'^login$',login),
    url(r'^email_login$',email_login),
    url(r'^face_login$',face_login),
    url(r'^register$',register),
    # url(r'^test_register.html$',register),
    url(r'^email_register$',email_register),
    url(r'^face_register$',face_register),
    # url(r'^save_email_register$',save_email_register),
    # url(r'^(?P<elogin_id>[0-9]+)/email_login/$',email_login),
    url(r'^registration_form$',registerform),

    
]



