from django.urls import include, path
from rest_framework import routers

from .views import (CommentViewSet, FollowViewSet, GroupReadOnlyViewSet,
                    PostViewSet)

app_name = "api"

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet, basename="posts")
router.register(r"groups", GroupReadOnlyViewSet, basename="groups")
router.register(r"follow", FollowViewSet, basename="groups")
router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comments"
)


urlpatterns = [
    path("v1/", include("djoser.urls.jwt")),
    path("v1/", include(router.urls)),
]
