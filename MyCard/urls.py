from django.contrib import admin
from django.urls import include, path
from polls.views import loginpage
from polls.views import base
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('polls.urls')),
    path('admin/', admin.site.urls),
]


urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)