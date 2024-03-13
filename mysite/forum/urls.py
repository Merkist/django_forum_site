from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('/posts/<post_id>', views.post, name='posts'),
    path('/add_post', views.create_post, name='add_post'),
]
