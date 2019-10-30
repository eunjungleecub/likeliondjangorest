from rest_framework import viewsets
from .models import Writing, Photo, Files
from .serializers import WritingSerializer, PhotoSerializer, FilesSerializer
from rest_framework.filters import SearchFilter
#parser
from rest_framework.parsers import MultiPartParser, FormParser

class PostViewSet(viewsets.ModelViewSet):

#manually initialize
    queryset = Writing.objects.all()
    serializer_class = WritingSerializer

    filter_backends = [SearchFilter]
    search_fields = ('title','body')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

#restrict permission
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            qs=qs.filter(author=self.request.user)
        else:
            qs = qs.none()
        return qs

class PhotosViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    filter_backends = [SearchFilter]
    search_fields = ('caption')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

#HTTP status response
from rest_framework.response import Response
from rest_framework import status

class FilesViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer

    filter_backends = [SearchFilter]
    search_fields = ('title')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# parsers for files uploads
    parser_classes = (MultiPartParser, FormParser)

#overriding create method
    def post(self, request, *args, **kwargs):
        serializer = FilesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=HTTP_400_BAD_REQUEST)
