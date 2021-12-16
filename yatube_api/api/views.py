from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny

from posts.models import Group, Post
from .permissions import IsAuthorOrReadOnlyPermission
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class GetCreateDeleteViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    pass


class GetViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    pass


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthorOrReadOnlyPermission,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = None
    permission_classes = (IsAuthorOrReadOnlyPermission,)

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        new_queryset = post.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)


class GroupReadOnlyViewSet(GetViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = None
    permission_classes = (AllowAny,)


class FollowViewSet(GetCreateDeleteViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ("following__username",)
    pagination_class = None

    def get_queryset(self):
        new_queryset = self.request.user.follower
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
