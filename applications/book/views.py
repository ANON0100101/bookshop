from rest_framework import generics
from applications.book.models import CustomUser
from applications.book.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from applications.book.permissions import IsOwnerAdminOrReadOnly


class ListPostView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerAdminOrReadOnly]



class CreatePostView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RetrievePostView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]



class UpdatePostView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerAdminOrReadOnly]

class DeletePostView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerAdminOrReadOnly]
