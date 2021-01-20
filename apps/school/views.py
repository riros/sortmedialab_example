from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from school.models import EUser, Score
from school.serializers import EUserSerializer, ScoreSerializer


class LargeResultSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 10000


class SmallResultSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10000


class NoPagination(PageNumberPagination):
    page_size = None


class EUserViewSet(viewsets.ModelViewSet):
    queryset = EUser.objects.all()
    serializer_class = EUserSerializer

    pagination_class = SmallResultSetPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    ordering_fields = ('username', 'user_type')

    rels = (
        'exact',
        'contains',
        'gt', 'gte', 'lt', 'lte',
        'in', 'regex', 'isnull',
    )
    filterset_fields = {
        'id': ('exact', "in"),
        'username': ('icontains',),
        'email': rels,
        'abs_score': ('gt', 'gte', 'lt', 'lte', 'exact'),
        'user_type': ('exact',),
        'birth_day': ('gt', 'gte', 'lt', 'lte', 'exact')

    }
    search_fields = ('username', 'user_type')


class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

    pagination_class = LargeResultSetPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    ordering_fields = ('index',)

    rels = (
        'exact',
        'contains',
        'gt', 'gte', 'lt', 'lte',
        'in', 'regex', 'isnull',
    )
    filterset_fields = {
        'id': ('exact', "in"),
        'name': ('icontains',),
        'index': ('gt', 'gte', 'lt', 'lte', 'exact'),
        'short_name': ('exact',),

    }
    search_fields = ('name',)
