from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, GroupViewSet, FollowViewSet, CommentViewSet

router = DefaultRouter()

router.register('groups', GroupViewSet)
router.register('posts', PostViewSet)
router.register('follow', FollowViewSet, basename='follow')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment',
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/auth/', include('djoser.urls')),
]
