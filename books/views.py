from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from handlers.pagination import PaginationPage
from .models import Book
from .serializers import BookSerializer
from django.core.cache import cache

class BookListCreateView(GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = PaginationPage

    def get(self, request, *args, **kwargs):
        books = cache.get('books_list')
        if not books:
            books = list(self.get_queryset())
            cache.set('books_list', books, timeout=3600)

        page = self.paginate_queryset(books)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BookDetailUpdateDeleteView(GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        book_id = self.kwargs.get(self.lookup_url_kwarg)
        cache_key = f'book_{book_id}'
        book = cache.get(cache_key)
        if not book:
            book = get_object_or_404(self.get_queryset(), pk=book_id)
            serializer = self.get_serializer(book)
            cache.set(cache_key, serializer.data, timeout=3600)
        else:
            serializer = self.get_serializer(book)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        book = self.get_object()
        serializer = self.get_serializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        book = self.get_object()
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
