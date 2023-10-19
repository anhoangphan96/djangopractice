from django.contrib import admin
from . import models

# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    fields = [
        "release_year",
        "title",
        "length",
    ]
    search_fields = ["release_year", "length"]
    list_filter = ["release_year", "title"]
    list_display = [
        "release_year",
        "title",
        "length",
    ]
    list_editable = ["length"]


admin.site.register(models.Movie, MovieAdmin)

admin.site.register(models.Customer)
