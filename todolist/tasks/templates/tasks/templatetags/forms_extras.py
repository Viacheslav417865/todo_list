from django import template
from crispy_forms.utils import render_crispy_form

register = template.Library()


@register.filter
def crispy(value):
    return render_crispy_form(value)
