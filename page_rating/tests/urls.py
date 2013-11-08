"""URLs to run the tests."""
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$',
        TemplateView.as_view(template_name='test.html'),
        name='test_page_rating'),
    url(r'', include('page_rating.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
