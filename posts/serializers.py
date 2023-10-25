from rest_framework import serializers
from .models import Post, User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'  # Ici à la place de __all__ on peut mentionner les champs qu'on désire : fields = ['title', 'body']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']