## Create

```python
>>> from bookshelf.models import Book
>>> Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# <Book: Book object (1)>

## Retrieve

```python
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
# 1984 George Orwell 1949

## Update

```python
book.title = "Nineteen Eighty-Four"
book.save()
book.title
# 'Nineteen Eighty-Four'

## Delete

```python
book.delete()
Book.objects.all()
# <QuerySet []>



