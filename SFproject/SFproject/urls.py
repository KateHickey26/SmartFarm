from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from KirktonApp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
                  # this maps the url to the home view in the KirktonApp app
                  path('', views.home, name='home'),
                  path('KirktonApp/', include('KirktonApp.urls')),
                  path('accounts/', include('registration.backends.simple.urls')),
                  path('admin/', admin.site.urls),
              ] + staticfiles_urlpatterns()

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.PROJECT_DIR + 'static')
#     urlpatterns += static('/templates/', document_root=settings.PROJECT_DIR + '/templates/')
