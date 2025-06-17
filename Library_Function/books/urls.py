from django.urls import path
from . import views

app_name = 'books'  # important for namespacing

urlpatterns = [
    path('',views.home,name='home'),
    path('addbook/', views.add_book, name='addbook'),
    path('addbook1/', views.add_book_user, name='addbook1'),
    path('viewbook/', views.BookView, name='viewbook'),
    path('book_detail/<int:pk>/', views.book_detail, name='book_detail'),
    path('edit_book/<int:pk>/',views.edit_book,name='edit_book'),
    path('deletebook/<int:pk>/', views.delete_book, name='delete_book'),
    path('search/',views.searchbook,name='searchbook'),
]
