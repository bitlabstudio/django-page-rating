"""Admin classes for the page_rating app."""
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Rating, UserRating


class RatingAdmin(admin.ModelAdmin):
    """Custom admin for the ``Rating`` model."""
    list_display = ['page_url', 'page_query', 'upvotes', 'downvotes']
    search_fields = ['page_url', 'page_qurey']


class UserRatingAdmin(admin.ModelAdmin):
    """Custom admin for the ``UserRating`` model."""
    list_display = ['creation_date', 'ip', 'user', 'vote']

    def vote(self, obj):
        if obj.is_positive:
            return 'up'
        else:
            return 'down'
    vote.short_description = _('Vote')


admin.site.register(Rating, RatingAdmin)
admin.site.register(UserRating, UserRatingAdmin)
