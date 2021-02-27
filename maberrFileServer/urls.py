from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/v1/', include('feedsAPI.urls')),
]
