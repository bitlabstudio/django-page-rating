"""Setting defaults for the ``page_rating`` app."""
from django.conf import settings

DEFAULT_TEMPLATE = getattr(settings, 'PAGE_RATING_DEFAULT_TEMPLATE',
                           'page_rating/page_rating.html')
