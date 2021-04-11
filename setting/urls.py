from django.contrib import admin
from django.urls import path, include
from mysite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mysite.urls')),
]
