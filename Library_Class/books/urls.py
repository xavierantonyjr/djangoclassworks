from django.urls import path
from . import views

app_name = 'books'  # important for namespacing

urlpatterns = [
    path('', views.BookHomeView.as_view(), name='home'),
    path('addbook/', views.AddBookView.as_view(), name='addbook'),
    path('addbook1/', views.AddBookUserView.as_view(), name='addbook1'),
    path('viewbook/', views.ViewBooks.as_view(), name='viewbook'),
    path('detail/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('updatebook/<int:pk>/', views.EditBookView.as_view(), name='edit_book'),
    path('deletebook/<int:pk>/', views.DeleteBookView.as_view(), name='delete_book'),
    path('search/', views.SearchBookView.as_view(), name='SearchBookView'),
]
