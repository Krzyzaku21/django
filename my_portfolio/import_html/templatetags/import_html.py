from django import template
from import_html.models import ImportHtml
from django.views import View

register = template.Library()


def import_html(custom_id):
    html = ImportHtml.objects.get(id=custom_id)
    return {'html': html}


register.inclusion_tag('../templates/import_html.html')(import_html)
