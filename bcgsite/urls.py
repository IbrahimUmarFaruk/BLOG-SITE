from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # User Authentication (Login/Logout)
    path('accounts/', include('django.contrib.auth.urls')),

    # Connects to your "core" app
    path('', include('core.urls')),
]

# This allows images to be seen while you are developing the site
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
