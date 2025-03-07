from django.contrib import admin
from django.urls import path
from principal.views import principal_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('principal/', principal_view),
]
