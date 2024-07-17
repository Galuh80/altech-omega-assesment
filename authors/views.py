from rest_framework import status, generics
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from handlers.pagination import PaginationPage
from .models import Author
from .serializers import AuthorSerializer
from books.serializers import BookSerializer
from django.core.cache import cache

class AuthorListCreateView(GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = PaginationPage

    def get(self, request, *args, **kwargs):
        # Cache the author
        authors = cache.get('authors_list')
        if not authors:
            authors = list(self.get_queryset())
            cache.set('authors_list', authors, timeout=3600)

        page = self.paginate_queryset(authors)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AuthorDetailUpdateDeleteView(GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        author_id = self.kwargs.get(self.lookup_url_kwarg)
        # Cache detail with the author
        cache_key = f'author_{author_id}'
        author = cache.get(cache_key)
        if not author:
            author = get_object_or_404(self.get_queryset(), pk=author_id)
            serializer = self.get_serializer(author)
            cache.set(cache_key, serializer.data, timeout=3600)
        else:
            serializer = self.get_serializer(author)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        author = self.get_object()
        serializer = self.get_serializer(author, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        author = self.get_object()
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AuthorBookListView(GenericAPIView):
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        author_pk = self.kwargs.get('pk') 
        author = get_object_or_404(Author, pk=author_pk)
        
        # Cache books associated with the author
        cache_key = f'author_books_{author_pk}'
        cached_books = cache.get(cache_key)
        if cached_books is None:
            books = author.books.all()
            cached_books = BookSerializer(books, many=True).data
            cache.set(cache_key, cached_books, timeout=3600)
        
        return Response(cached_books, status=status.HTTP_200_OK)