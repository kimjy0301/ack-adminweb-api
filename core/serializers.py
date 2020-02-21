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

