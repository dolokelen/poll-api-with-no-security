from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='category')
router.register('questions', views.QuestionViewSet, basename='question')

urlpatterns = [
    path('hello', views.hello),
    path('', include(router.urls))
]