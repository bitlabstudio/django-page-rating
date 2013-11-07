"""Factories for the page_rating app."""
import factory

from ..models import Rating, UserRating


class RatingFactory(factory.django.DjangoModelFactory):
    """Factory for the ``Rating`` model."""
    FACTORY_FOR = Rating

    page_url = factory.Sequence(lambda n: '/page_url/{0}/'.format(n))


class UserRatingFactory(factory.django.DjangoModelFactory):
    """Factory for the ``UserRating`` model."""
    FACTORY_FOR = UserRating

    ip = factory.Sequence(lambda n: '123.123.123.{0}'.format(n))
    is_positive = True
    rating = factory.SubFactory(RatingFactory)
