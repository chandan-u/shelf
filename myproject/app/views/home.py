from django.http import Http404
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template


def home(request, self):
    try:
        return direct_to_template(request, template="login.hmtl")
    except TemplateDoesNotExist:
        raise Http404()






