"""Tests for the views of the ``page_rating`` app."""
from django.test import TestCase

from django_libs.tests.factories import UserFactory
from django_libs.tests.mixins import ViewTestMixin

from ..factories import RatingFactory


class RatingSubmitViewTestCase(ViewTestMixin, TestCase):
    """Tests for the ``RatingSubmitView`` view class."""
    longMessage = True

    def get_view_name(self):
        return 'page_rating_submit'

    def setUp(self):
        self.user = UserFactory()
        self.rating = RatingFactory(page_url='foo/bar/',
                                    page_query='rab=oof')
        self.rating_without_query = RatingFactory(page_url='foo/')

        self.data = {
            'page_url': self.rating.page_url,
            'page_query': self.rating.page_query,
            'yes': 'YES',
            'ip': '127.0.0.1',
        }

        self.alternative_data = {
            'page_url': self.rating_without_query.page_url,
            'page_query': '',
            'no': 'NO',
            'ip': '',
        }

    def test_view(self):
        self.is_callable(method='post', data=self.data)
        self.is_callable(method='post', data=self.alternative_data,
                         user=self.user)
