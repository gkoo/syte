# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render, redirect
from django.template import Context, loader
from django.http import HttpResponseServerError
from django.views.decorators.cache import never_cache

from syte.context_processor import site_pages


@never_cache
def server_error(request, template_name='500.html'):
    t = loader.get_template(template_name)
    d = site_pages(request)
    return HttpResponseServerError(t.render(Context(d)))


@never_cache
def page_not_found_error(request, template_name='404.html'):
    t = loader.get_template(template_name)
    d = site_pages(request)
    return HttpResponseServerError(t.render(Context(d)))

def shuttle(request):
  return redirect('http://gkoo.github.com/shuttle')


def home(request):
    return render(request, 'index.html', {
      'blog_platform': settings.BLOG_PLATFORM,
      'wp_blog_url': settings.WORDPRESS_BLOG_URL
    })
