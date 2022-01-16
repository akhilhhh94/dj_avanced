from django.core.exceptions import ValidationError


def validate_even(value):
    value = set(f"{value}".lower().split())
    print(value)
    if len(value & set(["bad", "dad"])) > 0:
        raise ValidationError(
            ('%(value)s is not an even number'),
            params={'value': len(list(value & set(["bad", "dad"])))},
        )