from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",              include(        "main.urls")),
    path("contributors/", include("contributors.urls")),
    path("editors/",      include(     "editors.urls")),
    path("categories/",   include(  "categories.urls")),
    path("contact/",      include(     "contact.urls")),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
