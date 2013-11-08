"""Views for the page_rating app."""
from django.views.generic import View
from django.shortcuts import redirect

from .models import Rating, UserRating


class RatingSubmitView(View):

    def post(self, request, *args, **kwargs):
        page_url = request.POST.get('page_url')
        page_query = request.POST.get('page_query')
        ip = request.POST.get('ip')
        if request.user.is_authenticated():
            user = request.user
        else:
            user = None
        is_positive = 'yes' in request.POST
        rating = Rating.objects.get(page_url=page_url, page_query=page_query)

        # increase the up or downvotes for this rating
        if is_positive:
            rating.upvotes += 1
        elif not is_positive:
            rating.downvotes += 1
        rating.save()

        # create a rating entry for the user
        UserRating.objects.create(
            user=user, rating=rating, is_positive=is_positive, ip=ip,
        )

        # store the current page in the user's session
        # for simplicity we only concatenate the path and the query string,
        # without the ?. So this will not be a valid for use as url.
        rated_pages = request.session.get('rated_pages', [])
        rated_pages.append(page_url + page_query)
        request.session['rated_pages'] = rated_pages

        if page_query:
            get_data = '?{0}'.format(page_query)
        else:
            get_data = ''
        return redirect('{0}{1}'.format(page_url, get_data))
