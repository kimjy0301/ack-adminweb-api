from rest_framework import serializers


class ServerStatusSerializer(serializers.BaseSerializer):
    cpu = serializers.CharField()
    total_memory = serializers.CharField()
    free_memory = serializers.CharField()
    percent_memory = serializers.CharField()
    total_disk = serializers.CharField()
    free_disk = serializers.CharField()
    percent_disk = serializers.CharField()

    def to_representation(self, instance):
        return {
            "total_disk": instance.get("total_disk", None),
            "free_disk": instance.get("free_disk", None),
            "percent_disk": instance.get("percent_disk", None),
            "used_disk": instance.get("used_disk", None),
            "total_memory": instance.get("total_memory", None),
            "free_memory": instance.get("free_memory", None),
            "percent_memory": instance.get("percent_memory", None),
            "used_memory": instance.get("used_memory", None),
            "cpu": instance.get("cpu", None),
        }


class AtypeStatusSerializer(serializers.BaseSerializer):
    philipsStatus = serializers.CharField()
    medianaStatus = serializers.CharField()
    MindrayStatus = serializers.CharField()

    def to_representation(self, instance):
        return {
            "philipsStatus": instance.get("philipsStatus", None),
            "medianaStatus": instance.get("medianaStatus", None),
            "MindrayStatus": instance.get("MindrayStatus", None),
        }


class EmrifYearSerializer(serializers.BaseSerializer):
    month = serializers.CharField()
    send_count = serializers.IntegerField()
    error_count = serializers.IntegerField()

    def to_representation(self, instance):
        returndata = []
        for monthData in instance:
            data = {
                "month": monthData.get("month", None),
                "send_count": monthData.get("send_count", None),
                "error_count": monthData.get("error_count", None),
            }
            returndata.append(data)
        return returndata


class EmrifWeekSerializer(serializers.BaseSerializer):
    send_count = serializers.IntegerField()
    error_count = serializers.IntegerField()

    def to_representation(self, instance):
        return {
            "send_count": instance.get("send_count", None),
            "error_count": instance.get("error_count", None),
        }


class EmrifDeptSerializer(serializers.BaseSerializer):
    dept = serializers.CharField()
    send_count = serializers.IntegerField()
    error_count = serializers.IntegerField()

    def to_representation(self, instance):
        returndata = []
        for monthData in instance:
            data = {
                "dept": monthData.get("dept", None),
                "send_count": monthData.get("send_count", None),
                "error_count": monthData.get("error_count", None),
            }
            returndata.append(data)
        return returndata
