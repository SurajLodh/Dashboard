from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('app1.urls')),
    # path('', include('REST.urls'))
]
