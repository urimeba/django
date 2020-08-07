from django.contrib import admin
from django.urls import path, include
from Apps.oneSampleApp import urls as urls_oneSampleApp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls_oneSampleApp))
]
