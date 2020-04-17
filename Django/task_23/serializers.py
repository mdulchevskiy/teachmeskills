from rest_framework import serializers
from task_23.models import Fio


class FioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fio
        fields = ('id', 'name', 'surname')
