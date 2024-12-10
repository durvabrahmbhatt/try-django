from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView


urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='books'),
    path('register/', views.register, name='register'),
    path('add_book/', views.add_book, name='add_book'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),  # Book detail page
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),  # Edit book route
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),  # Delete book route
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.custom_logout, name='logout'), 
]
