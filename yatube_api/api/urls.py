from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()
router.register("posts", PostViewSet)
router.register("groups", GroupViewSet)
router.register(
    r"posts/(?P<post_id>\d+)/comments",
    CommentViewSet, basename="comment"
)

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/api-token-auth/", obtain_auth_token),
]
