from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from catalog.views import ContactsView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('contacts/', ContactsView.as_view(), name='contacts'),
                  path('', include('catalog.urls', namespace='catalog')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
