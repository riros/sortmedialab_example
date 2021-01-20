from typing import List, Type

from django.db.models import ManyToManyField, ManyToManyRel, ManyToOneRel, Model


def all_fields_without_fk(model: Type[Model], *args, **kwargs) -> List:
    exclude: List = kwargs.get("exclude", [])
    include_related: bool = kwargs.get("include_related", False)

    # тут нельзя исопльзовать вычитания через set, происходит сортировка полей

    names = [
        field.name
        for field in model._meta.get_fields()
        if type(field) not in (ManyToManyField, ManyToOneRel, ManyToManyRel) or include_related
    ]
    for name in names:
        if name in exclude:
            names.remove(name)
    return names
