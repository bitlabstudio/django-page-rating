"""URLs for the page_rating app."""
from django.conf.urls.defaults import patterns, url

from .views import RatingSubmitView


urlpatterns = patterns(
    '',
    url(r'^rating-submit/$', RatingSubmitView.as_view(),
        name='page_rating_submit'),
)
