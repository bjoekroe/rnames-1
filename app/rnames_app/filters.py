# https://django-filter.readthedocs.io/en/master/guide/usage.html
# If you want to access the filtered objects in your views,
# for example if you want to paginate them, you can do that.
# They are in f.qs
import django_filters as filters

from .models import (Binning
    , Location
    , Name
    , Qualifier
    , Binning
    , QualifierName
    , Reference
    , Relation
    , StratigraphicQualifier
    , StructuredName
    , TimeScale
    , AbsoluteAgeValue
    , BinningAbsoluteAge)
from django.contrib.auth.models import User
from django.db.models import Q

class TimeScaleFilter(filters.FilterSet):
    ts_name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = TimeScale
        fields = ['ts_name', ]

class LocationFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Location
        fields = ['name', ]

class NameFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Name
        fields = ['name', ]

class QualifierFilter(filters.FilterSet):
    qualifier_name__name = filters.CharFilter(lookup_expr='icontains')
    stratigraphic_qualifier__name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Qualifier
        fields = ['qualifier_name__name','stratigraphic_qualifier__name', ]

class QualifierNameFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = QualifierName
        fields = ['name', ]

class RelationFilter(filters.FilterSet):
    name = filters.CharFilter(method='evaluate_both_names', label ='Filter both names')

    name_one__name__name = filters.CharFilter(lookup_expr='icontains')
    name_two__name__name = filters.CharFilter(lookup_expr='icontains')
    reference__doi = filters.CharFilter(lookup_expr='icontains')
    reference__title = filters.CharFilter(lookup_expr='icontains')

    def evaluate_both_names(self, queryset, name, value):
        return queryset.filter(Q(name_one__name__name__icontains=value) | Q(name_two__name__name__icontains=value))

    class Meta:
        model = Relation
        fields = ['name_one__name__name', 'name_two__name__name', 'belongs_to', 'reference__doi', 'reference__title' ]

class ReferenceFilter(filters.FilterSet):
    first_author = filters.CharFilter(lookup_expr='icontains')
    title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Reference
        fields = ['first_author', 'year', 'title', ]

class StratigraphicQualifierFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = StratigraphicQualifier
        fields = ['name', ]

class StructuredNameFilter(filters.FilterSet):
    qualifier__qualifier_name__name = filters.CharFilter(lookup_expr='icontains')
    qualifier__stratigraphic_qualifier__name = filters.CharFilter(lookup_expr='icontains')
    name__name = filters.CharFilter(lookup_expr='icontains')
    location__name = filters.CharFilter(lookup_expr='icontains')
    reference__doi = filters.CharFilter(lookup_expr='icontains')
    reference__title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = StructuredName
        fields = ['name__name','qualifier__qualifier_name__name','qualifier__stratigraphic_qualifier__name','location__name', 'reference__doi', 'reference__title' ]

class UserFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', ]


class APINameFilter(filters.FilterSet):
#    name = filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Name
        fields = ['name', 'created_by__first_name', ]

class AbsoluteAgeValueFilter(filters.FilterSet):
    structured_name__name__name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = AbsoluteAgeValue
        fields = ['structured_name__name__name']

class BinningFilter(filters.FilterSet):
    binning_scheme__ts_name = filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Binning
        fields = ['binning_scheme__ts_name', 'binning_scheme']

class BinningResultsBaseFilter(filters.FilterSet):
    structured_name__qualifier__qualifier_name__name = filters.CharFilter(lookup_expr='icontains')
    structured_name__qualifier__stratigraphic_qualifier__name = filters.CharFilter(lookup_expr='icontains')
    structured_name__name__name = filters.CharFilter(lookup_expr='icontains')
    structured_name__location__name = filters.CharFilter(lookup_expr='icontains')

class BinningResultsFilter(BinningResultsBaseFilter):
    class Meta:
        fields = ['structured_name__name__name','structured_name__qualifier__qualifier_name__name',
            'structured_name__qualifier__stratigraphic_qualifier__name','structured_name__location__name']
        model = Binning

class BinningAbsoluteAgeResultsFilter(BinningResultsBaseFilter):
    class Meta:
        fields = BinningResultsFilter.Meta.fields
        model = BinningAbsoluteAge