from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.urls import reverse_lazy

from .forms import BookForm
from .models import Book
from django.views import View

# class BookhomeView(View):
#     def get(self, request):
#         return render(request, 'index.html')
#
#     def post(self, request):
#         return render(request, 'index.html')

class BookHomeView(View):
    def get(self, request):
        return render(request, 'index.html')

class BookView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'viewbook.html', {'books': books})

    def post(self, request):
        form_instance = BookForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('books:home')
        return render(request, 'addbook.html', {'form': form_instance})


class AddBookView(View):
    def get(self, request):
        form_instance = BookForm()
        return render(request, 'addbook.html', {'form': form_instance})

    def post(self, request):
        form_instance = BookForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('books:home')
        return render(request, 'addbook.html', {'form': form_instance})

class AddBookUserView(View):
    def get(self, request):
        form_instance = BookForm()
        return render(request, 'addbook1.html', {'form': form_instance})
    def post(self, request):
        t = request.POST['t']
        a = request.POST['a']
        n = request.POST['n']
        l = request.POST['l']
        p = request.POST['p']
        i = request.FILES['i']
        b = Book.objects.create(title=t, author=a, price=n, language=l, pages=p, image=i)
        b.save()
        return render(request, 'addbook1.html')

class ViewBooks(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'viewbook.html', {'books': books})

class BookDetailView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'book_detail.html', {'book': book})

class EditBookView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form_instance = BookForm(instance=book)
        return render(request, 'edit_book.html', {'form': form_instance})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form_instance = BookForm(request.POST, request.FILES, instance=book)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('books:viewbook')
        return render(request, 'edit_book.html', {'form': form_instance})

from django.views.generic.edit import DeleteView
class DeleteBookView(DeleteView):
    model = Book
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('books:home')

class SearchBookView(View):
    def get(self, request):
        return render(request, 'search.html')

    def post(self, request):
        query = request.POST.get('q', '').strip()
        print('Search query:', query)

        books = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(language__icontains=query)
        )

        print(f"Found books: {books}")
        return render(request, 'search.html', {'books': books, 'query': query})
