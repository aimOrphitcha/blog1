from django.shortcuts import render_to_response
from blogpost.models import Blogpost
from blogpost.forms import BlogpostForm
from django.template.context_processors import csrf


def index(request):

    blog = Blogpost.objects.all()
    form = BlogpostForm()
    data = {'blog_list': blog, 'blogpost_form': form}
    data.update(csrf(request))
    if request.POST:
        post = BlogpostForm(request.POST)
        if post.is_valid:
            post.save()
    return render_to_response('index.html', data)
