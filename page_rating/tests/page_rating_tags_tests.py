"""Tests for the template tags of the ``page_rating`` app."""
from django.template import Context
from django.test import TestCase
from django.test.client import RequestFactory

from ..models import Rating
from ..templatetags.page_rating_tags import render_rating


class RenderRatingTestCase(TestCase):
    longMessage = True

    def test_tag(self):
        req = RequestFactory().get('/?foo=bar')
        req.session = {}
        context = Context({'request': req})

        render_rating(context)
        self.assertEqual(Rating.objects.count(), 1, msg=(
            'The tag should have created one Rating object.'))

        req.META = {'HTTP_X_FORWARDED_FOR': '127.0.0.1, 0.0.0.0'}
        req.session = {'rated_pages': ['/foo=bar']}
        context = Context({'request': req})
        render_rating(context)
        self.assertEqual(Rating.objects.count(), 1, msg=(
            'The tag should not have created another Rating object.'))
        rating = Rating.objects.get()
        self.assertEqual(rating.page_views, 2, msg=(
            'The tag has not increased the pge views properly.'))
