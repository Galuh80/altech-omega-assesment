from django.urls import path
from .views import (
    AuthorListCreateView, 
    AuthorDetailUpdateDeleteView, 
)

urlpatterns = [
    path('authors', AuthorListCreateView.as_view(), name='author-list'),
    path('authors/<int:pk>', AuthorDetailUpdateDeleteView.as_view(), name='author-detail'),
]
