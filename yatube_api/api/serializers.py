from django.shortcuts import get_object_or_404
from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = "__all__"
        model = Post
        read_only_fields = ("author",)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )

    class Meta:
        fields = "__all__"
        model = Comment
        read_only_fields = (
            "author",
            "post",
        )


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "title", "slug", "description")


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )
    following = serializers.StringRelatedField()

    class Meta:
        model = Follow
        fields = ("user", "following")

    def validate(self, data):
        if "following" not in self.context["request"].data:
            raise serializers.ValidationError("Отсутствует параметр following")
        following = get_object_or_404(
            User, username=self.context["request"].data.get("following")
        )
        if Follow.objects.filter(
            user=self.context["request"].user, following=following
        ).exists():
            raise serializers.ValidationError("Подписка уже существует")
        if self.context["request"].user == following:
            raise serializers.ValidationError(
                "Нельзя подписываться на самого себя"
            )
        return data

    def create(self, validated_data):
        following = get_object_or_404(
            User, username=self.context['request'].data.get("following"))
        follow = Follow.objects.create(
            user=validated_data["user"], following=following)
        return follow
