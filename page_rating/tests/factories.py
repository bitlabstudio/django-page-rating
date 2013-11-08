"""Factories for the page_rating app."""
# so we got conflicting factory-boy version requirements. I'd rather use the
# 2.0.0+ version here, but django-libs requires factory-boy<2.0.0 resulting in
# v1.3.0
import factory
try:
    from factory.django import DjangoModelFactory as Factory
except ImportError:
    from factory import Factory

from ..models import Rating, UserRating


class RatingFactory(Factory):
    """Factory for the ``Rating`` model."""
    FACTORY_FOR = Rating

    page_url = factory.Sequence(lambda n: '/page_url/{0}/'.format(n))


class UserRatingFactory(Factory):
    """Factory for the ``UserRating`` model."""
    FACTORY_FOR = UserRating

    ip = factory.Sequence(lambda n: '123.123.123.{0}'.format(n))
    is_positive = True
    rating = factory.SubFactory(RatingFactory)
