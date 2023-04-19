from django_filters import rest_framework as filters
from .models import Livro

class LivroFilter(filters.FilterSet):

    nome = filters.CharFilter(field_name='nome',lookup_expr="icontains")
    editora = filters.CharFilter(field_name='editora',lookup_expr="icontains")

    class Meta:
        model = Livro
        fields = ('nome','editora')