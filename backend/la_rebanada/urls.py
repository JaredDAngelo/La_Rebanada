from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('productos.urls')),
    path('api/', include('users.urls')),
    path('api/fidelizacion/', include('fidelizacion.urls')),
    path('api/carrito/', include('carrito.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
