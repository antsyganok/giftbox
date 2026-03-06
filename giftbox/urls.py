from django.urls import path, include
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.catalog.urls'))
]


handler404 = 'apps.core.views.page_not_found'
handler500 = 'apps.core.views.server_error'
handler403 = 'apps.core.views.permission_denied'
settings.CSRF_FAILURE_VIEW = 'apps.core.views.csrf_failure'
