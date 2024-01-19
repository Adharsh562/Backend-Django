from django.db import models

# Create your models here.
# library/models.py


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=20)
    # Add more fields as needed

class Patron(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    # Add more fields as needed



class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)
    check_out_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    # library/models.py


class Patron(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

