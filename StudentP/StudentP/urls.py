from django.contrib import admin
from django.urls import path, include
from StudentP import views
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header="Welcome to our world!"
admin.site.site_title="xxx"
admin.site.index_title="FEATURES"

urlpatterns = [
    path('', views.homePage),
    path('admin/', admin.site.urls),
    path('about-us', views.aboutus),
    path('create_user', views.create_user),
    path('feedback', views.feedback),
    path('App/',include('App.urls'))
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


