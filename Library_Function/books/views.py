from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .forms import BookForm
from .models import Book


def home(request):
    return render(request, 'index.html')

def add_book(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        form_instance = BookForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            # b = Book.objects.create(
            #     title=form_instance.cleaned_data['title'],
            #     author=form_instance.cleaned_data['author'],
            #     price=form_instance.cleaned_data['price'],
            #     language=form_instance.cleaned_data['language'],
            #     pages=form_instance.cleaned_data['pages'],
            #     image=form_instance.cleaned_data['image']
            # )
            # b.save()
            return redirect('books:home')

    form_instance = BookForm()
    return render(request, 'addbook.html', {'form': form_instance})


def add_book_user(request):
    if request.method == 'POST':
        # print(request.POST)
        # print(request.FILES)
        t = request.POST['t']
        a = request.POST['a']
        n = request.POST['n']
        l = request.POST['l']
        p = request.POST['p']
        i = request.FILES['i']
        b = Book.objects.create(title=t, author=a, price=n, language=l, pages=p, image=i)
        b.save()
        return render(request, 'addbook1.html')

    return render(request, 'addbook1.html')

def BookView(request):
        books = Book.objects.all()
        return render(request, 'viewbook.html', {'books': books})

def search(request):
    return render(request, 'search.html')

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'book_detail.html', {'book': book})

def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    form_instance = BookForm(request.POST,request.FILES,instance=book)
    if form_instance.is_valid():
            form_instance.save()
            return redirect('books:viewbook')
    else:
        form_instance = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form_instance})

def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('books:home')
from django.shortcuts import render
from django.db.models import Q
from .models import Book

def searchbook(request):
    books = None
    if request.method == "POST":
        query = request.POST.get('q', '').strip()
        print(f"Search query: {query}")

        # Search title, author, language with case-insensitive partial match
        books = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(language__icontains=query)
        )
        print(f"Found books: {books}")

    return render(request, 'search.html', {'books': books})


