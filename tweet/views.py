from rest_framework import viewsets
from tweet.serializers import TwitSerializer
from tweet.models import Tweet
# Create your views here.


class TwitViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TwitSerializer