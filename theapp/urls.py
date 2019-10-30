from rest_framework.routers import DefaultRouter
from django.urls import path, include
from theapp import views

router = DefaultRouter()
router.register('writings', views.PostViewSet)
router.register('photos', views.PhotosViewSet)
router.register('files', views.FilesViewSet)

urlpatterns =[
    path('', include(router.urls))
]