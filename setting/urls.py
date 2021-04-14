from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from mysite import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('', include('mysite.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    prefix_default_language=False

)