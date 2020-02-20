from rest_framework import serializers
from .models import EmrifPc, EmrifEquip, EmrifDept, EmrifError, EmrifLab


class EmrifDeptSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmrifDept
        fields = [
            "id",
            "name",
        ]


class EmrifLabSerializer(serializers.ModelSerializer):
    dept = EmrifDeptSerializer()

    class Meta:
        model = EmrifLab
        fields = [
            "id",
            "name",
            "dept",
            "call_number",
        ]


class EmrifEquipSerializer(serializers.ModelSerializer):
    lab = EmrifLabSerializer()

    class Meta:
        model = EmrifEquip
        fields = [
            "id",
            "lab",
            "name",
            "equip_company",
            "equip_name",
            "equip_number",
        ]


class EmrifPcSerializer(serializers.ModelSerializer):
    equip = EmrifEquipSerializer(read_only=True)

    class Meta:
        model = EmrifPc
        fields = [
            "id",
            "ip",
            "equip",
            "status",
        ]


class EmrifErrorSerializer(serializers.ModelSerializer):
    pc = EmrifPcSerializer(read_only=True)

    class Meta:
        model = EmrifError
        fields = [
            "id",
            "pc",
            "title",
            "content",
        ]

