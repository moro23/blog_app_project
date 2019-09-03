from django.urls import path

from .views import BlogListView, BlogDetailsView

urlpatterns = [
    path('post/<int:pk>/',  BlogDetailsView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
]