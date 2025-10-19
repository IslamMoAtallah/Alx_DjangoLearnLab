from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
get_user_model().objects.create_user
class UserSerializer(serializers.ModelSerializer):
    follower_count = serializers.IntegerField(source='follower_count', read_only=True)
    following_count = serializers.IntegerField(source='following_count', read_only=True)
    class Meta:
        model = user
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'follower_count', 'following_count']
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,min_length=8)
    Token = serializers.CharField(read_only=True)
    class Meta:
        model = user
        fields = ['id', 'username', 'email', 'password']
    def create(self, validated_data):
        user = user.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        Token.objects.create(user=user)  # Create a token for the new user
        return user
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)
class UserListSerializer(serializers.ModelSerializer):
    follower_count = serializers.IntegerField(source='follower_count', read_only=True)
    following_count = serializers.IntegerField(source='following_count', read_only=True)
    is_following = serializers.SerializerMethodField()
    class Meta:
        model = user
        fields = '__all_'
    def get_is_following(self, obj):
        request = self.context.get('request')
        if not request or request.user.is_anonymous:
            return False
        return obj in request.user.following.all()


