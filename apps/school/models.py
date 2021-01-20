from datetime import date

from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.db.models import CharField, DateField, ForeignKey, IntegerField, PROTECT

from example.models import BaseModel


class EUser(AbstractUser, BaseModel):
    UNSET = 0
    STUDENT = 1
    TEACHER = 2
    DIRECTOR = 3
    STUFF = 4
    USER_TYPE = (
        (UNSET, 'Не задано'),
        (STUDENT, 'Ученик'),
        (TEACHER, 'Учитель'),
        (DIRECTOR, 'Директор'),
        (STUFF, 'Персонал')
    )
    user_type = IntegerField(choices=USER_TYPE, default=UNSET, verbose_name='тип пользователя')
    abs_score = ForeignKey('Score', on_delete=PROTECT, verbose_name='успеваемость', null=True, blank=True)

    birth_day = DateField(verbose_name='дата рождения', default=date(1900, 1, 1))

    middle_name = CharField(max_length=255, verbose_name='Отчество', default=None, null=True, blank=True)

    def __str__(self):
        return ''.join([self.first_name, self.last_name, self.middle_name])


class Score(BaseModel):
    index = IntegerField(verbose_name='числовое значение оценки')
    name = CharField(max_length=50, verbose_name='наименование')
    short_name = CharField(max_length=10, verbose_name='сокращение')

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
