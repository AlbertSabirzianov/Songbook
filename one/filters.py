import django_filters as filters


class SongFilter(filters.FilterSet):
    """Фильтрация песен."""

    have_score = filters.CharFilter(method='filter_have_score')
    band1 = filters.NumberFilter(method='filter_band')
    style1 = filters.NumberFilter(method='filter_style')
    name = filters.CharFilter(lookup_expr='icontains')
    wrigth = filters.CharFilter(lookup_expr='icontains')
    transcription = filters.CharFilter(lookup_expr='icontains')

    def filter_have_score(self, qs, name, value):
        """Фильтруем по наличию партитуры."""

        if value == 'on':
            return qs.filter(have_score=True)
        return qs

    def filter_band(self, qs, name, value):
        """Фильтруем по составу."""

        if value == 0:
            return qs
        return qs.filter(band=value)

    def filter_style(self, qs, name, value):
        """Фильтруем по стилю."""

        if value == 0:
            return qs
        return qs.filter(style=value)
