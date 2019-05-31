from blog.models import Post
from django.contrib.auth.models import User
from rest_framework import serializers, exceptions


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("username", "first_name", "last_name", "email")

        model = User


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    tags = serializers.SlugRelatedField(many=True, slug_field="name", read_only=True)
    date_posted = serializers.DateTimeField(read_only=True)

    def create(self, context):
        post = Post(user=self.context["request"].user, **context)
        post.save()
        return post

    class Meta:
        fields = ("title", "date_posted", "user", "desc", "tags")

        model = Post
