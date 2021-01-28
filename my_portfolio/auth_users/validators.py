from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from datetime import date


def validate_image(value):
    width_field = value.width
    height_field = value.height
    if width_field > 250 and height_field > 250:
        raise ValidationError('Image must be lower than 250 pixels')


def no_future_date(value):
    today = date.today()
    if value > today:
        raise ValidationError('Birth date cannot be in the future.')


class CustomPasswordValidator():

    def __init__(self, min_length=1):
        self.min_length = min_length

    def validate(self, password, user=None):
        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
        if not any(char.isdigit() for char in password):
            raise ValidationError(_('Password must contain at least %(min_length)d digit.') %
                                  {'min_length': self.min_length})
        if not any(char.isalpha() for char in password):
            raise ValidationError(_('Password must contain at least %(min_length)d letter.') %
                                  {'min_length': self.min_length})
        if not any(char in special_characters for char in password):
            raise ValidationError(
                _('Password must contain at least %(min_length)d special character.') %
                {'min_length': self.min_length})

    def get_help_text(self):
        return ""
