from django.db import models
from core.models import CoreModel


class EmrifDept(CoreModel):
    id = models.AutoField(db_column="ID", primary_key=True)
    name = models.CharField(db_column="NAME", max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "EMRIF_DEPT"

    def __str__(self):
        return self.name


class EmrifEquip(CoreModel):
    id = models.AutoField(db_column="ID", primary_key=True)
    lab = models.ForeignKey(
        "EmrifLab", models.DO_NOTHING, db_column="LAB_ID", blank=True, null=True
    )
    name = models.CharField(db_column="NAME", max_length=50, blank=True, null=True)
    equip_company = models.CharField(
        db_column="EQUIP_COMPANY", max_length=50, blank=True, null=True
    )
    equip_name = models.CharField(
        db_column="EQUIP_NAME", max_length=50, blank=True, null=True
    )
    equip_number = models.CharField(
        db_column="EQUIP_NUMBER", max_length=50, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "EMRIF_EQUIP"

    def __str__(self):
        return self.name


class EmrifError(CoreModel):
    id = models.AutoField(db_column="ID", primary_key=True)
    pc = models.ForeignKey(
        "EmrifPc", models.DO_NOTHING, db_column="PC_ID", blank=True, null=True
    )
    title = models.CharField(db_column="TITLE", max_length=500, blank=True, null=True)
    content = models.CharField(
        db_column="CONTENT", max_length=2000, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "EMRIF_ERROR"

    def __str__(self):
        return self.name


class EmrifLab(CoreModel):
    id = models.AutoField(db_column="ID", primary_key=True)
    name = models.CharField(db_column="NAME", max_length=50, blank=True, null=True)
    dept = models.ForeignKey(
        EmrifDept, models.DO_NOTHING, db_column="DEPT_ID", blank=True, null=True
    )
    call_number = models.CharField(
        db_column="CALL_NUMBER", max_length=50, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "EMRIF_LAB"

    def __str__(self):
        return self.name


class EmrifPc(CoreModel):
    id = models.AutoField(db_column="ID", primary_key=True)
    ip = models.CharField(db_column="IP", max_length=50, blank=True, null=True)
    equip = models.ForeignKey(
        EmrifEquip, models.DO_NOTHING, db_column="EQUP_ID", blank=True, null=True
    )
    status = models.CharField(db_column="STATUS", max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "EMRIF_PC"
        ordering = [
            "status",
        ]

    def __str__(self):
        return f"{self.ip} / {self.equip}"
