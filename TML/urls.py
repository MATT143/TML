
from django.contrib import admin
from django.urls import path,include
from taskManagementLayer import urls as tmlurls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(tmlurls)),
]
