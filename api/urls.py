from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()

router.register(r'bookmarks', views.BookmarkViewSet)
router.register(r'commands', views.CommandVIewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
