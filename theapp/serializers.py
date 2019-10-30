from .models import Writing, Photo, Files
from rest_framework import serializers

#writings
class WritingSerializer(serializers.ModelSerializer):
    
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Writing
        fields = ('pk','title','body','author_name')

#photos
class PhotoSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='author.username')
    img = serializers.ImageField(use_url=True)

    class Meta:
        model = Photo
        fields = ('pk','title','caption','img','author_name')

#files
class FilesSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='author.username')
    files = serializers.FileField(use_url=True)

    class Meta:
        model = Files
        fields = ('pk','title','files','author_name')