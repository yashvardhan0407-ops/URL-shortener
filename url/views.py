
import random
import string

from django.shortcuts import render, redirect, get_object_or_404

from .models import UrlData
from .forms import Url


def urlShort(request):

    if request.method == 'POST':

        form = Url(request.POST)

        if form.is_valid():

            url = form.cleaned_data['url']

            slug = ''.join(
                random.choice(string.ascii_letters + string.digits)
                for _ in range(10)
            )

            new_url = UrlData(
                url=url,
                slug=slug
            )

            new_url.save()

            # Get all saved URLs
            data = UrlData.objects.all()

            context = {
                'form': Url(),
                'data': data,
                'latest': new_url
            }

            return render(request, 'index.html', context)

    else:
        form = Url()

    data = UrlData.objects.all()

    context = {
        'form': form,
        'data': data
    }

    return render(request, 'index.html', context)


def urlRedirect(request, slugs):

    data = get_object_or_404(UrlData, slug=slugs)

    return redirect(data.url)

