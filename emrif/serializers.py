from rest_framework import serializers
from .models import EmrifPc, EmrifEquip, EmrifDept, EmrifError, EmrifLab, EmrifAib


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
        fields = ["id", "name", "dept", "call_number", "bg_image", "floor"]


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
    send_count = serializers.SerializerMethodField()
    error_count = serializers.SerializerMethodField()

    class Meta:
        model = EmrifPc
        fields = [
            "id",
            "ip",
            "equip",
            "status",
            "send_count",
            "error_count",
            "position_left",
            "position_top",
        ]

    def get_error_count(self, obj):
        request = self.context.get("request")

        startdate = request.GET.get("startdate", None)
        enddate = request.GET.get("enddate", None)
        try:
            if startdate and enddate:
                count = obj.emriferror.filter(
                    created__date__range=[startdate, enddate],
                ).count()
            else:
                count = obj.emriferror.count()
        except Exception:
            count = obj.emriferror.count()

        return count

    def get_send_count(self, obj):
        request = self.context.get("request")
        startdate = request.GET.get("startdate", None)
        enddate = request.GET.get("enddate", None)
        try:
            if startdate and enddate:
                count = obj.emrifaib.filter(
                    created__date__range=[startdate, enddate],
                ).count()
            else:
                count = obj.emrifaib.count()
        except Exception:
            count = obj.emrifaib.count()

        return count


class EmrifErrorSerializer(serializers.ModelSerializer):
    emrifpc = EmrifPcSerializer(read_only=True)
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = EmrifError
        fields = ["id", "emrifpc", "title", "content", "state_flag", "created"]


class EmrifAIBSerializer(serializers.ModelSerializer):
    emrifpc = EmrifPcSerializer(read_only=True)

    class Meta:
        model = EmrifAib
        fields = [
            "id",
            "emrifpc",
        ]
