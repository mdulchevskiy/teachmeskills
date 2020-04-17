from django.shortcuts import render, redirect
from shortener.models import Shortener
from shortener.forms import ShortenerForm
from random import choice
import string


def generate_key():
    chars = string.digits + string.ascii_letters
    rand_url = ''.join(choice(chars) for _ in range(6))
    return rand_url


def shorten_url(request):
    urls = Shortener.objects.filter()
    if request.method == 'POST':
        form = ShortenerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            long_url = data['long_url']
            shortening_method = data['shortening_method']
            if shortening_method == 'manual':
                short_url = data['manual_shortening']
                if not short_url.isalnum():
                    message = 'Wrong shortening!'
                    return render(request, 'home_page.html', {'form': form, 'message': message, 'urls': urls})
            else:
                short_url = generate_key()
            all_short_urls = [url.short_url for url in urls]
            if short_url in all_short_urls:
                message = 'This short URL has already exist!'
                return render(request, 'home_page.html', {'form': form, 'message': message, 'urls': urls})
            else:
                Shortener.objects.create(long_url=long_url, short_url=short_url)
                return redirect('home_page')
        else:
            return render(request, 'home_page.html', {'form': form, 'urls': urls})
    return render(request, 'home_page.html', {'form': ShortenerForm(), 'urls': urls})


def redirect_short_url(request, short_url):
    long_url = Shortener.objects.filter(short_url=short_url)[0].long_url
    clicks = Shortener.objects.filter(short_url=short_url)[0].clicks + 1
    Shortener.objects.filter(short_url=short_url).update(clicks=clicks)
    return redirect(long_url)


def delete_short_url(request, url_id):
    Shortener.objects.filter(id=url_id).delete()
    return redirect('home_page')
