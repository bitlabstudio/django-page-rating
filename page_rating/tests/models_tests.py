"""Tests for the models of the page_rating app."""
from django.test import TestCase

from .factories import RatingFactory, UserRatingFactory


class RatingTestCase(TestCase):
    """Tests for the ``Rating`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test instantiation of the ``Rating`` model."""
        rating = RatingFactory()
        self.assertTrue(rating.pk)


class UserRatingTestCase(TestCase):
    """Tests for the ``UserRating`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test instantiation of the ``UserRating`` model."""
        userrating = UserRatingFactory()
        self.assertTrue(userrating.pk)
