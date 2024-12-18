from api.permissions import OwnerOrReadOnly
from api.serializers import CommentSerializer, GroupSerializer, PostSerializer
from posts.models import Comment, Group, Post
from rest_framework import viewsets


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (OwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (OwnerOrReadOnly,)

    def get_post_id(self):
        return self.kwargs.get("post_id")

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.get_post_id())

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post_id=self.get_post_id())
