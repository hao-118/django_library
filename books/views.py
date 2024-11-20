from django.shortcuts import render, get_object_or_404

from .forms import UserRegistrationForm
from .models import Book
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # 假设你有一个登录视图
    else:
        form = UserRegistrationForm()
    return render(request, 'books/register.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, isbn):
    book = get_object_or_404(Book, isbn=isbn)
    return render(request, 'books/book_detail.html', {'book': book})