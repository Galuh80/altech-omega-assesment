from django.urls import path
from .views import (
    AuthorListCreateView, 
    AuthorDetailUpdateDeleteView, 
    AuthorBookListView
)

urlpatterns = [
    path('authors', AuthorListCreateView.as_view(), name='author-list'),
    path('authors/<int:pk>', AuthorDetailUpdateDeleteView.as_view(), name='author-detail'),
    path('authors/<int:pk>/books', AuthorBookListView.as_view(), name='author-books-list'),
]
