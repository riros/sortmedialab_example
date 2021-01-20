# from rest_framework_json_api import serializers

from rest_framework import serializers

from school.models import EUser, Score


class EUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EUser
        fields = (
            'id',
            'user_type',
            'abs_score',
        )


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Score
        fields = (
            'id',
            'index',
            'name',
            'short_name',
        )
