from django.contrib import admin
from django.urls import path, include

uarlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('web.urls'))
]
