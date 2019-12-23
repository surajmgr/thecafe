from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
import mainapp.views

handler404 = mainapp.views.error_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls'), name='home'),
]
