from django.urls import path
from django.contrib import admin
from . import views

app_name = 'library'

urlpatterns = [
    path('admin/',admin.site.urls),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/<int:book_id>/update/', views.book_update, name='book_update'),
    path('books/<int:book_id>/delete/', views.book_delete, name='book_delete'),

    path('patrons/', views.patron_list, name='patron_list'),
    path('patrons/<int:patron_id>/', views.patron_detail, name='patron_detail'),
    path('patrons/create/', views.patron_create, name='patron_create'),
    path('patrons/<int:patron_id>/update/', views.patron_update, name='patron_update'),
    path('patrons/<int:patron_id>/delete/', views.patron_delete, name='patron_delete'),

    # Add URL patterns for loans
    path('loans/', views.loan_list, name='loan_list'),
    path('loans/<int:loan_id>/', views.loan_detail, name='loan_detail'),
    path('loans/create/', views.loan_create, name='loan_create'),
    path('loans/<int:loan_id>/update/', views.loan_update, name='loan_update'),
    path('loans/<int:loan_id>/return/', views.loan_return, name='loan_return'),
]
