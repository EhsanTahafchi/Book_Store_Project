from django.contrib import admin
from django.urls import path, include
from .views import BookListView, BookCreateView, BookUpdateView, BookDeleteView, book_detail_view, book_search, \
    favourite_book, favourite_book_list

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', book_detail_view, name='book_detail'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('search/', book_search, name='book_search'),
    path('<int:pk>/favourite_book/', favourite_book, name='favourite_book'),
    path('favourite_book_list/', favourite_book_list, name='favourite_book_list'),

]
