
from typing import ValuesView
from unicodedata import name
from django.urls.resolvers import URLPattern
from.import views
from django.urls import path

urlpatterns=[
    path('',views.home, name="homepage"),

    path('log',views.logi, name="loginpage"),

    path('sign',views.signi, name="signinpage" ),
]