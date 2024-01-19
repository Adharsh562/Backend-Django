# library/forms.py
from django import forms
from .models import Book, Patron, Loan

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

# Create similar forms for Patron and Loan

# library/forms.py



class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = '__all__'

# library/forms.py


class PatronForm(forms.ModelForm):
    class Meta:
        model = Patron
        fields = '__all__'

