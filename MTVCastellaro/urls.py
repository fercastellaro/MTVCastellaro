from django.contrib import admin
from django.urls import path
from AppFamiliares.views import padre, madre, hermano, hermanoMasChico

urlpatterns = [
    path('admin/', admin.site.urls),
    path('padre/', padre),
    path('madre/', madre),
    path('hermano/', hermano),
    path('hermanoMasChico/', hermanoMasChico),
]
