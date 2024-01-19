
# Create your views here.
# library/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

from .models import Patron
from .forms import PatronForm
from .models import Loan
from .forms import LoanForm
from datetime import datetime,timezone
# library/views.py

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'library/book_detail.html', {'book': book})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/book_form.html', {'form': form})

def book_update(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'library/book_form.html', {'form': form})

def book_delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'library/book_confirm_delete.html', {'book': book})



# Add views for update and delete as well











# library/views.py

from .models import Patron
from .forms import PatronForm

def patron_list(request):
    patrons = Patron.objects.all()
    return render(request, 'library/patron_list.html', {'patrons': patrons})

def patron_detail(request, patron_id):
    patron = get_object_or_404(Patron, pk=patron_id)
    return render(request, 'library/patron_detail.html', {'patron': patron})

def patron_create(request):
    if request.method == 'POST':
        form = PatronForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patron_list')
    else:
        form = PatronForm()
    return render(request, 'library/patron_form.html', {'form': form})

def patron_update(request, patron_id):
    patron = get_object_or_404(Patron, pk=patron_id)
    if request.method == 'POST':
        form = PatronForm(request.POST, instance=patron)
        if form.is_valid():
            form.save()
            return redirect('patron_list')
    else:
        form = PatronForm(instance=patron)
    return render(request, 'library/patron_form.html', {'form': form})

def patron_delete(request, patron_id):
    patron = get_object_or_404(Patron, pk=patron_id)
    if request.method == 'POST':
        patron.delete()
        return redirect('patron_list')
    return render(request, 'library/patron_confirm_delete.html', {'patron': patron})


# library/views.py

from .models import Loan
from .forms import LoanForm

def loan_list(request):
    loans = Loan.objects.all()
    return render(request, 'library/loan_list.html', {'loans': loans})

def loan_detail(request, loan_id):
    loan = get_object_or_404(Loan, pk=loan_id)
    return render(request, 'library/loan_detail.html', {'loan': loan})

def loan_create(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loan_list')
    else:
        form = LoanForm()
    return render(request, 'library/loan_form.html', {'form': form})

def loan_update(request, loan_id):
    loan = get_object_or_404(Loan, pk=loan_id)
    if request.method == 'POST':
        form = LoanForm(request.POST, instance=loan)
        if form.is_valid():
            form.save()
            return redirect('loan_list')
    else:
        form = LoanForm(instance=loan)
    return render(request, 'library/loan_form.html', {'form': form})

def loan_return(request, loan_id):
    loan = get_object_or_404(Loan, pk=loan_id)
    if request.method == 'POST':
        loan.return_date = timezone.now()
        loan.save()
        return redirect('loan_list')
    return render(request, 'library/loan_return.html', {'loan': loan})
