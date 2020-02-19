from django.conf.urls import url
from django.urls import path, re_path
from app import views
from app.viewsdir.assetsAddForm import *
from app.viewsdir.loginForm import *
from app.viewsdir.regeditForm import *
from app.viewsdir.appInfoAddForm import *
urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.gentella_html, name='gentella'),

    # The home page
    path('', views.index, name='index'),
    url(r'assetsAddForm/$',assetsaddForm.as_view(),name='assetsadd'),
    url(r'login/$',login.as_view(),name='loginForm'),
    url(r'regeditForm/$',register.as_view(),name='regedit'),
    url(r'appInfoAddForm/$',appinfoAddForm.as_view(),name='appinfoAdd'),

]
