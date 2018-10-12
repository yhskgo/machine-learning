"""server_movierecsys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import re_path, include
from django.contrib import admin
admin.autodiscover()
from books_recsys_app.api import UsersList
from rest_framework_swagger.views import get_swagger_view
from books_recsys_app import views

schema_view = get_swagger_view(title='Recommend API')

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^docs/', schema_view),
    re_path(r'^$', views.home, name='home'),
    re_path(r'^auth/', views.auth, name='auth'),
    re_path(r'^signout/', views.signout, name='signout'),
    re_path(r'^rate_moview/', views.rate_movie, name='rate_movie'),
    re_path(r'^movies-recs/', views.movies_recs, name='movies_recs'),
    re_path(r'^users-list/', UsersList.as_view(), name='users-list'),
]
