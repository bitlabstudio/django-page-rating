"""Just an empty models file to let the testrunner recognize this as app."""
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Rating(models.Model):
    """
    This model maps the url and page query to the amount of up and downvotes.

    :downvotes: The positive integer representing the amount of downvotes.
    :page_query: The get data string sorted alphabetically after keys.
    :page_url: The relative path string of the url.
    :page_views: Positive integer for the amount of page views.
    :upvotes: The positive integer representing the amount of upvotes.

    """

    downvotes = models.PositiveIntegerField(
        verbose_name=_('Downvotes'),
        default=0,
    )

    page_query = models.CharField(
        verbose_name=_('Page query'),
        max_length=1024,
        blank=True,
    )

    page_url = models.CharField(
        verbose_name=_('Page url'),
        max_length=512,
    )

    page_views = models.PositiveIntegerField(
        verbose_name=_('Page views'),
        default=1,
    )

    upvotes = models.PositiveIntegerField(
        verbose_name=_('Upvotes'),
        default=0,
    )

    class Meta:
        unique_together = ('page_query', 'page_url')

    def __unicode__(self):  # pragma: nocover
        if self.page_query is not None:
            query = '?{0}'.format(self.page_query)
        return '{0}{1}'.format(self.page_url, query)


class UserRating(models.Model):
    """
    Represents the single vote of a user on a page.

    :creation_date: The date and time, this voting has been made.
    :ip: If we can retrieve it, holds the IP of a user. (optional)
    :is_positive: A boolean value being True for an upvote and False otherwise.
    :rating: FK to the Rating this UserRating belongs to.
    :user: FK to the user, that has voted, if logged in. (optional)

    """

    creation_date = models.DateTimeField(
        verbose_name=_('Creation Date'),
        auto_now_add=True,
    )

    ip = models.GenericIPAddressField(
        verbose_name=_('IP'),
        blank=True, null=True,
    )

    is_positive = models.BooleanField(
        verbose_name=_('Is positive'),
    )

    rating = models.ForeignKey(
        Rating,
        verbose_name=_('Rating'),
    )

    user = models.ForeignKey(
        'auth.User',
        verbose_name=_('User'),
        blank=True, null=True,
    )

    def __unicode__(self):  # pragma: nocover
        if self.is_positive:
            vote = 'up'
        else:
            vote = 'down'
        if self.user is not None:
            user = self.user
        elif self.ip:
            user = self.ip
        else:
            user = 'anonymous'
        return '{0}vote from {1}'.format(vote, user)
