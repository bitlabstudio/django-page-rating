"""Template tags for the ``page_rating`` app."""
from django.template import Library, loader

from ..models import Rating
from ..settings import DEFAULT_TEMPLATE

register = Library()


@register.simple_tag(takes_context=True)
def render_rating(context, template_name=DEFAULT_TEMPLATE):
    """
    Renders the rating form.

    Takes context and optional template_name as arguments.
    Template defaults to PAGE_RATING_DEFAULT_TEMPLATE setting.

    """
    # gathering the basic information
    request = context['request']
    page_url = request.path
    # this sorts the get parameters alphabetically via keys
    # it's split at "&" then sorted and then joined again with "&"
    page_query = '&'.join(sorted(request.GET.urlencode().split('&')))

    # getting the page rating object and incrementing the view counter
    rating, created = Rating.objects.get_or_create(
        page_url=page_url, page_query=page_query)
    if not created:
        rating.page_views += 1
        rating.save()

    # find out how many people found this page helpful
    total_votes = rating.upvotes + rating.downvotes
    try:
        percentage = round(float(rating.upvotes) / float(total_votes) * 100, 2)
    except ZeroDivisionError:
        percentage = None

    # get the list of urls, the user already voted on
    rated_pages = request.session.get('rated_pages', None)
    if rated_pages is None or page_url + page_query not in rated_pages:
        already_voted = 0
    else:
        already_voted = 1

    # get the user's IP
    # When we are e.g. on a webfaction apache, REMOTE_ADDR will be localhost,
    # so we first look into the HTTP_X_FORWARDED_FOR list and take the first
    # entry we find
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')

    context.update({'ip': ip, 'page_query': page_query,
                    'percentage': percentage, 'already_voted': already_voted})
    t = loader.get_template(template_name)
    return t.render(context)
