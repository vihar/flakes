from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^blog/', include('faded.urls')),
    url(r'^about/', TemplateView.as_view(template_name="about.html")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]
