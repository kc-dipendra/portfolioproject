from django.contrib import admin
from django.urls import path, include
from StudentP import views

urlpatterns = [
    path('', views.homePage),
    path('admin/', admin.site.urls),
    path('about-us', views.aboutus),
    path('create_user', views.create_user),
    path('feedback', views.feedback),
    path('App/',include('App.urls'))
]


