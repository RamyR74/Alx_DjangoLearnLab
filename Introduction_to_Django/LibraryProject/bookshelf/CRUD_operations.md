## Create

```python
>>> from bookshelf.models import Book
>>> Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# <Book: Book object (1)>

## Retrieve

```python
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="1984")
>>> print(book.title, book.author, book.publication_year)
# 1984 George Orwell 1949



## Update

```python
book.title = "Nineteen Eighty-Four"
book.save()
book.title
# 'Nineteen Eighty-Four'

## Delete

```python
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="Nineteen Eighty-Four")
>>> book.delete()
# (1, {'bookshelf.Book': 1})
>>> Book.objects.all()
# <QuerySet []>




