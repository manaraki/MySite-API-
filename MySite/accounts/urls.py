from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views
from .views import UserViewSet

app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegister.as_view(), name='register'),
]

# making an instance of SimpleRouter class
router = SimpleRouter()

# register UserViewSet in router
router.register('users', UserViewSet, basename='user')

# add router.urls to urlpatterns
urlpatterns += router.urls
