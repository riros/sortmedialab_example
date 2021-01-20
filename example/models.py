import uuid

from django.db.models.manager import BaseManager
from django.utils.timezone import now
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.db.models import BooleanField, DateTimeField, Model, QuerySet, UUIDField


class Manager(BaseManager.from_queryset(QuerySet)):
    pass


class NotDeletedManager(Manager):
    use_for_related_fields = True

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class BaseModel(Model):
    class Meta:
        abstract = True

    id = UUIDField(db_column='Id', primary_key=True, default=uuid.uuid4)

    created = DateTimeField(auto_now_add=True, db_index=True)
    updated = DateTimeField(auto_now=True, db_index=True)
    deleted = BooleanField(default=False, db_index=True)

    objects = NotDeletedManager()
    objects_all = Manager()


@receiver(pre_save, sender=BaseModel)
def _on_basemodel_pre_save(sender, instance, **kwargs):
    instance.updated = now()
