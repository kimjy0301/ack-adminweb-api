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
        "EmrifLab",
        models.DO_NOTHING,
        db_column="LAB_ID",
        blank=True,
        null=True,
        related_name="emrifequip",
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
    emrifpc = models.ForeignKey(
        "EmrifPc",
        models.DO_NOTHING,
        db_column="PC_ID",
        blank=True,
        null=True,
        related_name="emriferror",
    )
    title = models.CharField(db_column="TITLE", max_length=500, blank=True, null=True)
    content = models.CharField(
        db_column="CONTENT", max_length=2000, blank=True, null=True
    )

    state_flag = models.CharField(
        max_length=50, db_column="STATE_FLAG", blank=True, null=True,
    )

    class Meta:
        managed = False
        db_table = "EMRIF_ERROR"

    def __str__(self):
        return f"{str(self.id)} / {self.title}"


class EmrifLab(CoreModel):
    id = models.AutoField(db_column="ID", primary_key=True)
    name = models.CharField(db_column="NAME", max_length=50, blank=True, null=True)
    dept = models.ForeignKey(
        EmrifDept,
        models.DO_NOTHING,
        db_column="DEPT_ID",
        blank=True,
        null=True,
        related_name="emriflab",
    )
    call_number = models.CharField(
        db_column="CALL_NUMBER", max_length=50, blank=True, null=True
    )
    bg_image = models.ImageField(db_column="BG_IMAGE", blank=True, null=True)
    floor = models.CharField(db_column="FLOOR", max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "EMRIF_LAB"

    def __str__(self):
        return self.name


class EmrifPc(CoreModel):
    id = models.AutoField(db_column="ID", primary_key=True)
    ip = models.CharField(db_column="IP", max_length=50, blank=True, null=True)
    equip = models.ForeignKey(
        EmrifEquip,
        models.DO_NOTHING,
        db_column="EQUP_ID",
        blank=True,
        null=True,
        related_name="emrifpc",
    )
    status = models.CharField(db_column="STATUS", max_length=50, blank=True, null=True)
    position_left = models.IntegerField(
        db_column="POSITION_LEFT", blank=True, null=True
    )
    position_top = models.IntegerField(db_column="POSITION_TOP", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "EMRIF_PC"
        ordering = [
            "status",
        ]

    def __str__(self):
        return f"{self.ip} / {self.equip}"


class EmrifAib(models.Model):
    id = models.AutoField(db_column="ID", primary_key=True)
    pid = models.CharField(db_column="PID", max_length=10)
    rstseqno = models.IntegerField(db_column="RSTSEQNO")
    rstdate = models.CharField(db_column="RSTDATE", max_length=8)
    emrifpc = models.ForeignKey(
        "EmrifPc", models.DO_NOTHING, db_column="emrifpc", related_name="emrifaib"
    )

    state_flag = models.CharField(
        db_column="STATEFLAG", max_length=50, blank=True, null=True
    )
    created = models.DateTimeField(db_column="created")

    class Meta:
        managed = False
        db_table = "EMRIFAIB"

    def __str__(self):
        return f"PID = {self.pid}"
