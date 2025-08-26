from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),

    # agar aapke apps hain to unhe bhi include karna hoga
    # path('about/', include('aboutapp.urls')),
    # path('blogs/', include('blogsapp.urls')),
]

# Development ke liye static + media serve karne ke liye
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
