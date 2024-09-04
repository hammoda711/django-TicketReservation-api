"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from tickets import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register('guests', views.viewsets_guest)
router.register('movies', views.viewsets_movie)
router.register('reservations', views.viewsets_reservation)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Viewsets
    #http://127.0.0.1:8000/rest/viewsets/guests/
    path('rest/viewsets/', include(router.urls)),

    # find movie 
    path('fbv/findmovie', views.find_movie),

    # new reservation
    path('fbv/newreservation',views.new_reservation),

    # rest auth url
    #login\out
    path('api-auth', include('rest_framework.urls')),

    #Token auth --> access token model --> migrate
    path('api-token-auth', obtain_auth_token),

]
