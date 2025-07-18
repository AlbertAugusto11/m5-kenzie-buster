from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    readonly_fields = ("id", "is_superuser")

    fieldsets = (
        ("Credenciais", {"fields": ("username", "password")}),
        (
            "Personal Info",
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                )
            },
        ),
        ("Permissions", {"fields": ("is_employee", "is_superuser")}),
        ("Dates", {"fields": ("birthdate",)}),
    )


admin.site.register(User, CustomUserAdmin)
