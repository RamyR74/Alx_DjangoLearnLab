from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book



def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

def check_role(role):
    def inner(user):
        return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == role
    return user_passes_test(inner)

@login_required
@check_role('Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@check_role('Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@check_role('Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
