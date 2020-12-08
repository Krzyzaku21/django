from django import template
from customhtml.models import Customhtml

# przekaywanie kodu html przez baze danych
register = template.Library()

def render_html(custom_id):
    html = Customhtml.objects.get(id=custom_id)
    return {'html': html}

register.inclusion_tag('../templates/custom_html.html')(render_html)