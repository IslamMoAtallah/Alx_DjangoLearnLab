from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer
from rest_framework.decorators import api_view, permission_classes

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context={'request': request}).data,
            "token": user.token
        }, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data['username']
    password = serializer.validated_data['password']
    user = authenticate(request, username=username, password=password)
    if not user:
        return Response({"detail":"Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key, "user": UserSerializer(user, context={'request': request}).data})

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

@api_view(['POST'])
def follow_toggle(request, username):
    # toggle follow/unfollow target user
    try:
        target = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({"detail": "User not found"}, status=404)
    user = request.user
    if user == target:
        return Response({"detail":"You cannot follow yourself"}, status=400)
    if target.followers.filter(id=user.id).exists():
        target.followers.remove(user)
        action = 'unfollowed'
    else:
        target.followers.add(user)
        action = 'followed'
    return Response({"detail": action, "followers_count": target.follower_count()})
# Create your views here.
@permission_required('your_app.can_view', raise_exception=True)
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})
@permission_required('your_app.can_create', raise_exception=True)
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})
@permission_required('your_app.can_edit', raise_exception=True)
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/edit_post.html', {'form': form, 'post': post})
@permission_required('your_app.can_delete', raise_exception=True)
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'posts/delete_post.html', {'post': post})
book_list = Book.objects.all()
return render(request, 'books/book_list.html', {'books': book_list})
def book_list(request):
    book_list = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': book_list})

def post(self, request, user_id):
        target = get_object_or_404(User, id=user_id)
        if target == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(target)
        return Response({"detail": f"You are now following {target.username}."}, status=status.HTTP_200_OK)

    def delete(self, request, user_id):
        target = get_object_or_404(User, id=user_id)
        request.user.following.remove(target)
        return Response({"detail": f"You unfollowed {target.username}."}, status=status.HTTP_200_OK)


class FollowersListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        pk = self.kwargs.get('user_id')
        user = get_object_or_404(User, id=pk)
        return user.followers.all()  # users who follow 'user'


class FollowingListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        pk = self.kwargs.get('user_id')
        user = get_object_or_404(User, id=pk)
        return user.following.all()  # users whom 'user' follow
