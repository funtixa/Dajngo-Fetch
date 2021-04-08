from django.contrib import admin
from django.urls import path
from django_fetch.views import GetDroplets

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', GetDroplets.as_view(template_name='fetches.html'), name='Fetch View'),
]
