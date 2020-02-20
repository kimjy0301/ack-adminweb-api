from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm, CustomUserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ("userid", "date_of_birth", "is_admin")
    list_filter = ("is_admin",)

    fieldsets = (
        (None, {"fields": ("userid", "password"),}),
        ("Personal info", {"fields": ("date_of_birth",),}),
        ("Permission", {"fields": ("is_admin",),}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("userid", "password1", "password2", "date_of_birth"),
            },
        ),
    )

    search_fields = ("user_id",)
    ordering = ("userid",)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
