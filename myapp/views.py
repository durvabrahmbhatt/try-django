from django.shortcuts import render,redirect, get_object_or_404
from .models import Book
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from .forms import BookForm


def home(request):
    return render(request, 'myapp/home.html')

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp/book_list.html', {'books': books})

# This view will automatically display the login form and handle login functionality
class CustomLoginView(LoginView):
    template_name = 'registeration/login.html'

def custom_logout(request):
    logout(request)
    return redirect('login') 

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home') 
    else:
        form = RegistrationForm()
    return render(request, 'registeration/register.html', {'form': form})

@login_required 
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('books')  
    else:
        form = BookForm()

    return render(request, 'myapp/add_book.html', {'form': form})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('books')

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save() 
            return redirect('books')  
    else:
        form = BookForm(instance=book)

    return render(request, 'myapp/edit_book.html', {'form': form})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    return render(request, 'myapp/book_detail.html', {'book': book})
