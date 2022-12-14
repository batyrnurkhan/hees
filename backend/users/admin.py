from django.contrib import admin
from . import models
# Register your models here.
#123

class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "fullname",
        "last_name",
        "email"
    )

admin.site.register(models.User, UserAdmin)