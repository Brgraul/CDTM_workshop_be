# Create your views here.
from rest_framework import viewsets

from api.serializers import PostSerializer
from blog.models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
