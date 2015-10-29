from rest_framework import serializers
from tweet.models import Tweet


class TwitSerializer(serializers.ModelField):

    class Meta:
        model = Tweet
        fields = ('user', 'text', )
