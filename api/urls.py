
from django.conf.urls import include, url
from rest_framework import routers
from tweet.views import TwitViewSet

router = routers.DefaultRouter()
router.register(r'api/twits', TwitViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),

    # Auth
     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
