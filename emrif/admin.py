from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.EmrifPc)
class EmrifPcAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EmrifDept)
class EmrifDeptAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EmrifEquip)
class EmrifEquipAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EmrifError)
class EmrifErrorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EmrifLab)
class EmrifLabAdmin(admin.ModelAdmin):
    pass
