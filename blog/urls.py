from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name='blogger-detail'),
    path('bloggers', views.AuthorListView.as_view(), name='bloggers'),
    path('blog/<int:pk>/create/', views.create_comment, name='comment-create'),
]
