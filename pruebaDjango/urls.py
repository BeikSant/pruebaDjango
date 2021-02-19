
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estudiantes/', include('apps.gestion_estudiantes.urls')),
    path('notas/', include('apps.notas.urls')),
]
