from django.contrib.auth.password_validation import MinimumLengthValidator
from django.core.exceptions import ValidationError
from django.utils.translation import ngettext


class MinimumLengthValidator(MinimumLengthValidator):

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                ngettext(
                    "La contraseña ingresada es muy corta, debe tener al menos %(min_length)d caracteres.",
                    "La contraseña ingresada es muy corta, debe tener al menos %(min_length)d caracteres.",
                    self.min_length
                ),
                code='password_too_short',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return ngettext(
            "Your password must contain at least %(min_length)d character.",
            "Your password must contain at least %(min_length)d characters.",
            self.min_length
        ) % {'min_length': self.min_length}

