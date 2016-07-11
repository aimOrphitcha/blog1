from django.shortcuts import render_to_response
from django.template import RequestContext


def account_page(request):
    return render_to_response('account_page.html', context_instance=RequestContext(request))
