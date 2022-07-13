from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    
    fields = (
        'first_name',
        'last_name',
        'github_username',
        'email',
        'phone',
        'about',
        'is_active',
        'is_staff',
        'is_superuser',
    )
    read_only_fields = (
        'id',
        'date_joined',
    )

