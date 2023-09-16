import requests

from http import HTTPStatus
from django.core.exceptions import ValidationError


def url_path_validator(value: str):
    """
    Проверяем, доступна ли ссылка
    на музыкальный пример.
    """

    try:
        response = requests.get(url=value)
    except Exception:
        raise ValidationError(
            'Строка не является ссылкой!'
        )

    if response.status_code != HTTPStatus.OK:
        raise ValidationError(
            'Ссылка на музыкальный пример не доступна!'
        )
