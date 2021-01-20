from django.contrib import admin

# Register your models here.
# Register your models here.
from rangefilter.filter import DateRangeFilter

from example.utils import all_fields_without_fk
from school.models import EUser, Score


@admin.register(EUser)
class EUserAdmin(admin.ModelAdmin):
    list_display = all_fields_without_fk(EUser)
    search_fields = ["id"]
    list_filter = (
        ('birth_day', DateRangeFilter),
    )


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = all_fields_without_fk(Score)
    ordering = ('index',)

